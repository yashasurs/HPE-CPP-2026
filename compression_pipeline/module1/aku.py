import re
from spacy.matcher import DependencyMatcher
from constants import (
    NLP, TOKENIZER, BAD_SUBJECTS, BAD_OBJECTS, GENERIC_ENTITY_PHRASES,
    WEAK_ENTITY_HEADS, BAD_VERBS, GOOD_VERBS, VERB_NORMALIZATION,
    ACTION_PREFIXES, RESOURCE_QUALIFIERS, DOMAIN_RE, SPECIFIC_DOMAIN_RE,
    WORD_RE, CODE_RE, HTTP_RE, MAX_AKUS_PER_CHUNK, AKU_BATCH_SIZE,
)


# DEPENDENCY MATCHER


def setup_dependency_matcher():
    matcher = DependencyMatcher(NLP.vocab)
    direct_object = [
        {"RIGHT_ID": "verb", "RIGHT_ATTRS": {"POS": {"IN": ["VERB", "AUX"]}}},
        {
            "LEFT_ID": "verb",
            "REL_OP": ">",
            "RIGHT_ID": "subj",
            "RIGHT_ATTRS": {"DEP": {"IN": ["nsubj", "nsubjpass"]}},
        },
        {
            "LEFT_ID": "verb",
            "REL_OP": ">",
            "RIGHT_ID": "obj",
            "RIGHT_ATTRS": {"DEP": {"IN": ["dobj", "attr", "oprd"]}},
        },
    ]
    prep_object = [
        {"RIGHT_ID": "verb", "RIGHT_ATTRS": {"POS": {"IN": ["VERB", "AUX"]}}},
        {
            "LEFT_ID": "verb",
            "REL_OP": ">",
            "RIGHT_ID": "subj",
            "RIGHT_ATTRS": {"DEP": {"IN": ["nsubj", "nsubjpass"]}},
        },
        {
            "LEFT_ID": "verb",
            "REL_OP": ">",
            "RIGHT_ID": "prep",
            "RIGHT_ATTRS": {"DEP": {"IN": ["prep", "dative"]}},
        },
        {
            "LEFT_ID": "prep",
            "REL_OP": ">",
            "RIGHT_ID": "obj",
            "RIGHT_ATTRS": {"DEP": "pobj"},
        },
    ]
    matcher.add("DIRECT_SVO", [direct_object])
    matcher.add("PREP_SVO", [prep_object])
    return matcher


DEP_MATCHER = setup_dependency_matcher()

# UTILITY FUNCTIONS


def word_count(text):
    return len(WORD_RE.findall(text))


def is_code_noise(text):
    return bool(CODE_RE.search(text))


def is_http_noise(text):
    return bool(HTTP_RE.search(text))


def is_domain_phrase(text):
    return bool(DOMAIN_RE.search(text))


def is_specific_domain_phrase(text):
    return bool(SPECIFIC_DOMAIN_RE.search(text))


def is_bad_phrase(text):
    low = text.lower()
    return (
        "valid values" in low
        or "example" in low
        or low.startswith(("type ", "required ", "contents "))
        or low in {"type", "required", "contents"}
    )


def clean_phrase(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"^(the|a|an|this|that|these|those|your|their|our)\s+", "", text, flags=re.IGNORECASE)
    text = re.sub(r"(Amazon [A-Z][A-Za-z0-9 ]+ ){2,}", r"\1", text)
    text = re.sub(r"Amazon [A-Z][A-Za-z0-9 ]+ API Reference.*", "", text)
    text = re.sub(r"^[^A-Za-z0-9]+|[^A-Za-z0-9.)]+$", "", text)
    return text.strip()

# AKU FILTERING

def is_weak_subject(subject):
    low = subject.lower()
    return any(low.startswith(x) for x in (
        "this", "that", "these", "those", "it", "the request",
        "the operation", "the command", "the following",
    ))


def has_bad_entity_shape(text):
    low = text.lower().strip()
    words = WORD_RE.findall(low)

    if not words:
        return True
    if low in GENERIC_ENTITY_PHRASES:
        return True
    if words[0] in WEAK_ENTITY_HEADS and not is_specific_domain_phrase(text):
        return True
    if len(words) > 14:
        return True
    if len(words) == 1 and not is_specific_domain_phrase(text):
        return True

    alpha_chars = sum(ch.isalpha() for ch in text)
    if alpha_chars < 3:
        return True

    digit_chars = sum(ch.isdigit() for ch in text)
    if digit_chars > alpha_chars:
        return True

    return False


def normalize_aku_part(text):
    text = clean_phrase(text).lower()
    text = re.sub(r"[^a-z0-9 ]+", " ", text)
    text = re.sub(r"\b(the|a|an)\b", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    words = []
    for word in text.split():
        if len(word) > 3 and word.endswith("s"):
            word = word[:-1]
        words.append(word)
    return " ".join(words)


def canonical_aku_key(subject, verb, obj):
    return (normalize_aku_part(subject), verb.lower().strip(), normalize_aku_part(obj))


def normalize_verb(verb):
    verb = verb.lower().strip()
    return VERB_NORMALIZATION.get(verb, verb)


def is_incomplete(obj):
    return (
        (word_count(obj) < 2 and not is_specific_domain_phrase(obj))
        or obj.strip().lower().endswith(("the", "a", "an", "of", "to", "with", "for", "in", "by", "and", "or"))
    )


def score_aku(subject, verb, obj):
    score = 0

    if is_specific_domain_phrase(subject):
        score += 3
    elif is_domain_phrase(subject):
        score += 1
    if is_specific_domain_phrase(obj):
        score += 3
    elif is_domain_phrase(obj):
        score += 1
    if verb in GOOD_VERBS:
        score += 2
    elif verb not in BAD_VERBS:
        score += 1
    if 1 <= word_count(subject) <= 8:
        score += 1
    if 2 <= word_count(obj) <= 14:
        score += 1

    if is_code_noise(subject) or is_code_noise(obj):
        score -= 3
    if is_http_noise(obj):
        score -= 2
    if is_incomplete(obj):
        score -= 2
    if is_weak_subject(subject):
        score -= 4
    if is_bad_phrase(subject):
        score -= 2
    if has_bad_entity_shape(subject) or has_bad_entity_shape(obj):
        score -= 2
    if not is_specific_domain_phrase(subject + " " + obj):
        score -= 1
    if len(subject) > 8 and (subject.lower() in obj.lower() or obj.lower() in subject.lower()):
        score -= 3

    return score


def valid_aku(subject, verb, obj):
    subject = clean_phrase(subject)
    obj = clean_phrase(obj)
    verb = normalize_verb(verb)

    subject_low = subject.lower()
    obj_low = obj.lower()

    if not subject or not obj:
        return False
    if subject_low in BAD_SUBJECTS or obj_low in BAD_OBJECTS:
        return False
    if verb in BAD_VERBS:
        return False
    if has_bad_entity_shape(subject) or has_bad_entity_shape(obj):
        return False
    if word_count(subject) < 2 and not is_specific_domain_phrase(subject):
        return False
    if is_weak_subject(subject):
        return False
    if is_code_noise(subject) or is_code_noise(obj):
        return False
    if is_http_noise(obj):
        return False
    if is_incomplete(obj):
        return False
    if is_bad_phrase(subject):
        return False
    if not is_domain_phrase(subject + " " + obj):
        return False
    if normalize_aku_part(subject) == normalize_aku_part(obj):
        return False

    return score_aku(subject, verb, obj) >= 2

# AKU EXTRACTION

def expand_np(token, max_words=12):
    words = []
    for child in token.subtree:
        if child.is_punct or child.is_space or child.like_url or child.like_email:
            continue
        words.append(child.text)
    return clean_phrase(" ".join(words[:max_words]))


def objects_for_verb(token):
    objects = []
    for child in token.children:
        if child.dep_ in {"dobj", "attr", "oprd"}:
            objects.append(expand_np(child))
        elif child.dep_ in {"prep", "dative"}:
            for grandchild in child.children:
                if grandchild.dep_ == "pobj":
                    objects.append(expand_np(grandchild))
    return objects


def matcher_akus_from_sentence(sent):
    candidates = []
    sent_doc = sent.as_doc()
    for match_id, token_ids in DEP_MATCHER(sent_doc):
        label = NLP.vocab.strings[match_id]
        try:
            if label == "DIRECT_SVO":
                verb = sent_doc[token_ids[0]].lemma_
                subject = expand_np(sent_doc[token_ids[1]])
                obj = expand_np(sent_doc[token_ids[2]])
            elif label == "PREP_SVO":
                verb = sent_doc[token_ids[0]].lemma_
                subject = expand_np(sent_doc[token_ids[1]])
                obj = expand_np(sent_doc[token_ids[3]])
            else:
                continue
        except IndexError:
            continue

        candidates.append((subject, verb, obj))
    return candidates


def add_aku(akus, global_seen, subject, verb, obj):
    subject = clean_phrase(subject)
    obj = clean_phrase(obj)
    verb = normalize_verb(verb)

    if not valid_aku(subject, verb, obj):
        return

    key = canonical_aku_key(subject, verb, obj)
    if key in global_seen:
        return

    global_seen.add(key)
    akus.append([subject, verb, obj])


def trim_definition_object(obj, max_words=12):
    obj = clean_phrase(obj)
    obj = re.split(r"\s+(?:For more information|For details|Example:)\b", obj, maxsplit=1, flags=re.IGNORECASE)[0]
    obj = re.split(r"[;:]", obj, maxsplit=1)[0]
    words = obj.split()
    if len(words) > max_words:
        obj = " ".join(words[:max_words])
    return clean_phrase(obj)


def definition_akus_from_sentence(sentence):
    patterns = [
        r"^(.{3,120}?)\s+(?:is|are)\s+(?:a|an|the)?\s*(.{12,260})$",
        r"^(.{3,120}?)\s+(?:refers to|represents|means)\s+(.{12,260})$",
        r"^(.{3,120}?)\s+(?:provides|offers)\s+(.{12,220})$",
    ]

    for pattern in patterns:
        match = re.match(pattern, sentence, flags=re.IGNORECASE)
        if not match:
            continue

        subject = clean_phrase(match.group(1))
        obj = trim_definition_object(match.group(2))
        if is_domain_phrase(subject + " " + obj):
            return [[subject, "define", obj]]

    return []


def split_camel_name(name):
    name = re.sub(r"[_-]+", " ", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name)
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", name)
    return re.sub(r"\s+", " ", name).strip()


def resource_phrase_from_action(action_name, prefix):
    remainder = action_name[len(prefix):].strip()
    resource = split_camel_name(remainder)
    resource_low = resource.lower()

    for key, qualified in sorted(RESOURCE_QUALIFIERS.items(), key=lambda item: len(item[0]), reverse=True):
        if key in resource_low:
            return qualified

    if resource and is_specific_domain_phrase(resource):
        return f"{resource} resource"

    return ""


def action_akus_from_heading(heading_path):
    if not heading_path:
        return []

    title = heading_path[-1].strip()
    compact = re.sub(r"[^A-Za-z0-9]", "", title)
    if not compact or not compact[0].isupper():
        return []

    for prefix, verb in sorted(ACTION_PREFIXES.items(), key=lambda item: len(item[0]), reverse=True):
        if not compact.startswith(prefix) or len(compact) <= len(prefix):
            continue

        obj = resource_phrase_from_action(compact, prefix)
        if not obj:
            return []

        subject = f"{split_camel_name(compact)} API operation"
        return [[subject, verb, obj]]

    return []


def extract_akus_from_doc(doc, chunk):
    akus = []
    seen = set()

    for subject, verb, obj in action_akus_from_heading(chunk.get("heading_path", [])):
        add_aku(akus, seen, subject, verb, obj)

    for sent in doc.sents:
        sent_text = sent.text.strip()
        if not valid_sentence(sent_text):
            continue

        for subject, verb, obj in definition_akus_from_sentence(sent_text):
            add_aku(akus, seen, subject, verb, obj)

        for subject, verb, obj in matcher_akus_from_sentence(sent):
            add_aku(akus, seen, subject, verb, obj)

        for token in sent:
            if token.pos_ != "VERB":
                continue

            verb = normalize_verb(token.lemma_)
            subjects = [
                expand_np(child)
                for child in token.children
                if child.dep_ in {"nsubj", "nsubjpass"}
            ]
            objects = objects_for_verb(token)

            for subject in subjects:
                for obj in objects:
                    add_aku(akus, seen, subject, verb, obj)

    return sorted(
        akus,
        key=lambda aku: (-score_aku(*aku), aku[0].lower(), aku[1], aku[2].lower()),
    )[:MAX_AKUS_PER_CHUNK]


def extract_akus_batch(chunks):
    docs = NLP.pipe((chunk["text"] for chunk in chunks), batch_size=AKU_BATCH_SIZE)

    results = []
    for chunk, doc in zip(chunks, docs):
        akus = extract_akus_from_doc(doc, chunk)
        if akus:
            results.append({
                "chunk_id": chunk["chunk_id"],
                "akus": akus,
            })

    return results


def valid_sentence(sentence):
    from constants import MIN_SENT_WORDS, MAX_SENT_WORDS
    
    if sentence.startswith(("•", "-", "*")):
        return False
    words = word_count(sentence)
    if words < MIN_SENT_WORDS:
        return False
    if words > MAX_SENT_WORDS * 2:
        return False
    if is_code_noise(sentence) and not is_domain_phrase(sentence):
        return False
    if sentence.lower().startswith(("for more information", "the following", "this example")):
        return False
    return True

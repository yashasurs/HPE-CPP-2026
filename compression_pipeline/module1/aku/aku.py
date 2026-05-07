import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from spacy.matcher import DependencyMatcher
from config import (
    NLP,
    VERB_NORMALIZATION,
    AKU_BATCH_SIZE,
    MAX_NP_WORDS,
    MAX_AKUS,
    VERB_MAP as _VERB_MAP,
    COPULA_LEMMAS as _COPULA_LEMMAS,
    INVALID_ENTITIES as _INVALID_ENTITIES,
    GENERIC_HEAD_NOUNS as _GENERIC_HEAD_NOUNS,
    GENERIC_OBJECTS as _GENERIC_OBJECT_WORDS,
    NARRATIVE_TOKENS as _NARRATIVE_TOKENS,
    GENERIC_SHORT_SUBJECTS as _GENERIC_SHORT_SUBJECTS,
    NARRATIVE_OBJECT_PHRASES as _NARRATIVE_OBJECT_PHRASES,
    NP_NOISE_PREFIXES as _NP_NOISE_PREFIXES,
    LEADING_PREPS as _LEADING_PREPS,
    STOP_LAST_WORDS as _STOP_LAST,
    JUNK_RE as _JUNK_RE,
    GOOD_VERBS as _GOOD_VERBS,
    SPECIFIC_DOMAIN_RE as _SPECIFIC_DOMAIN_RE,
    SENT_REJECT_HTTP,
    SENT_REJECT_TIMESTAMP,
    SENT_REJECT_XML,
    SENT_REJECT_PATH,
    SENT_REJECT_SYMBOLS,
    SENT_REJECT_ELLIPSIS,
    SENT_REJECT_CONTINUATION,
    SENT_REJECT_PROCEDURAL,
    PHRASE_REJECT_DANGLING_PREP,
    PHRASE_REJECT_DATE_FRAG,
    PHRASE_REJECT_HTTP_VERB,
    PHRASE_REJECT_SLASH,
    PHRASE_REJECT_REL_CLAUSE,
    PHRASE_REJECT_AUX_CHAIN,
    COPULA_STRONG_HEADS,
    CONFIDENCE_WEIGHTS,
    CONFIDENCE_THRESHOLD,
)

# ── Camel-case detector for AWS API actions ────────────────────────────────────
_CAMEL_RE = re.compile(r"[A-Z][a-z]+[A-Z][a-z]+")
_XAMZ_RE = re.compile(r"^x-amz-", re.IGNORECASE)
_STOPWORD_RE = re.compile(
    r"^(a|an|the|this|that|these|those|its|their|our|your)\s+",
    re.IGNORECASE,
)
_UPPER_RATIO_THRESH = 0.5  # reject sentence if >50% tokens are ALL-CAPS non-AWS
_SENT_MIN_ALPHA_TOKENS = 4


# ── Controlled noun-phrase extraction ─────────────────────────────────────────

_NP_ALLOWED_DEPS = {
    "compound", "amod", "nmod", "poss", "nummod", "advmod",
    "appos", "flat", "fixed",
}
_NP_STOP_DEPS = {
    "relcl", "acl", "advcl", "csubj", "ccomp", "xcomp",
    "conj", "cc", "punct", "dep",
}

# POS tags that signal finite verb leakage inside a noun phrase
_FINITE_VERB_POS = {"VERB", "AUX"}
_CLAUSE_DEPS = {"relcl", "acl", "advcl", "csubj", "ccomp", "xcomp"}
_ADP_CHAIN_RE = re.compile(
    r"\b(of|in|to|for|by|on|at|from|with|about)\s+(of|in|to|for|by|on|at|from|with|about)\b",
    re.IGNORECASE,
)


def is_clean_np(span) -> bool:
    """
    Lightweight dependency-aware noun phrase validator.
    Runs AFTER regex cleanup and BEFORE AKU creation.

    Accepts spans that:
    - have exactly one noun/proper-noun head
    - contain no finite verbs (outside technical compound context)
    - contain no embedded clause fragments
    - contain no dangling ADP chains
    - contain no excessive punctuation

    Allows technical compound nouns (e.g., 'S3 Bucket Key', 'execution role').
    """
    if span is None:
        return False

    tokens = [t for t in span if not t.is_space]
    if not tokens:
        return False

    # Reject spans with 3+ punctuation tokens
    punct_count = sum(1 for t in tokens if t.is_punct)
    if punct_count >= 3:
        return False

    # Reject spans containing embedded clause dependencies
    for t in tokens:
        if t.dep_ in _CLAUSE_DEPS and t != span.root:
            return False

    # Reject spans containing finite verbs that are NOT the noun head
    # (allows participial compounds like "provisioned concurrency" via ADJ/VERB ambiguity)
    for t in tokens:
        if t.pos_ in _FINITE_VERB_POS and t.dep_ not in {"compound", "amod", "nmod"} and t != span.root:
            return False

    # Reject dangling ADP chains (e.g., "values of in the")
    span_text = " ".join(t.text for t in tokens)
    if _ADP_CHAIN_RE.search(span_text):
        return False

    # Require at least one noun or proper noun in the span
    has_noun = any(t.pos_ in {"NOUN", "PROPN"} for t in tokens)
    if not has_noun:
        return False

    return True


def _extract_np(token):
    """
    Controlled noun-phrase extraction.
    Walk only compound/modifier edges; stop at clause boundaries.
    Preserves CamelCase AWS API terms atomically.
    """
    # If token text is a CamelCase AWS action, return it verbatim.
    if _CAMEL_RE.search(token.text) and token.pos_ in {"NOUN", "PROPN"}:
        return token.text.strip()

    # Use spaCy noun chunks if available (more reliable than raw subtree).
    # Find the noun chunk containing this token's head noun.
    doc = token.doc
    for chunk in doc.noun_chunks:
        if chunk.root == token or chunk.root == token.head:
            if not is_clean_np(chunk):
                break  # fall through to controlled subtree
            text = _trim_np(chunk.text)
            if text:
                return text

    # Fallback: controlled subtree walk
    return _controlled_subtree(token)


def _controlled_subtree(token):
    """Walk subtree with dep-based stop conditions."""
    words = []
    for t in token.subtree:
        if t.is_punct or t.is_space:
            continue
        # Stop if we enter a relative/adverbial clause
        if t != token and t.dep_ in _NP_STOP_DEPS:
            break
        # Stop if we see a clause-introducing word
        if t.lower_ in {"that", "which", "who", "where", "when", "whose", "if", "whether"}:
            break
        words.append(t.text)
        if len(words) >= MAX_NP_WORDS:
            break

    text = " ".join(words).strip()
    return _trim_np(text)


def _trim_np(text):
    """Strip articles, trailing noise, and apply NP noise prefix removal."""
    text = re.sub(r"\s+", " ", text).strip()
    # Remove leading articles
    text = _STOPWORD_RE.sub("", text).strip()
    # Apply noise prefix patterns
    text = _NP_NOISE_PREFIXES.sub("", text).strip()
    # Strip trailing stop words
    words = text.split()
    while words and words[-1].lower() in _STOP_LAST:
        words.pop()
    text = " ".join(words).strip()
    # Strip leading prepositions
    words = text.split()
    while words and words[0].lower() in _LEADING_PREPS:
        words.pop(0)
    return " ".join(words).strip()


def _clean(t):
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"^[^A-Za-z0-9]+|[^A-Za-z0-9.]+$", "", t)
    return t.strip()


# ── Sentence-level quality gate ────────────────────────────────────────────────

def _sentence_is_clean(sent_text):
    """Return True only if sentence is safe to extract from."""
    t = sent_text.strip()

    if not t:
        return False

    # HTTP request lines
    if SENT_REJECT_HTTP.search(t):
        return False

    # Timestamps / date strings
    if SENT_REJECT_TIMESTAMP.search(t):
        return False

    # XML / HTML fragments
    if SENT_REJECT_XML.search(t):
        return False

    # Unix/URL path syntax
    if SENT_REJECT_PATH.search(t):
        return False

    # Symbol-heavy lines (query strings, code fragments)
    if SENT_REJECT_SYMBOLS.search(t):
        return False

    # Ellipsis / placeholder lines
    if SENT_REJECT_ELLIPSIS.search(t):
        return False

    # Continuation / forward-reference sentences
    if SENT_REJECT_CONTINUATION.search(t):
        return False

    # Procedural / instructional sentences
    if SENT_REJECT_PROCEDURAL.search(t):
        return False

    # Count tokens for structural check
    tokens = t.split()
    if len(tokens) < _SENT_MIN_ALPHA_TOKENS:
        return False

    # Too many ALL-CAPS tokens (likely header, code block, or table row)
    alpha_tokens = [tok for tok in tokens if tok.isalpha()]
    if alpha_tokens:
        upper_tokens = [tok for tok in alpha_tokens if tok.isupper() and len(tok) > 2]
        # Allow known AWS acronyms; reject if overwhelmingly uppercase
        if len(upper_tokens) / len(alpha_tokens) > _UPPER_RATIO_THRESH and len(upper_tokens) > 3:
            return False

    # Slash-heavy (path or HTTP syntax)
    slash_count = t.count("/")
    if slash_count >= 3:
        return False

    return True


# ── Phrase-level rejection ─────────────────────────────────────────────────────

def _phrase_is_clean(text):
    """Return True if phrase is structurally sound as an entity."""
    if not text or len(text) < 2:
        return False

    if PHRASE_REJECT_HTTP_VERB.match(text):
        return False

    if PHRASE_REJECT_DATE_FRAG.search(text):
        return False

    if PHRASE_REJECT_DANGLING_PREP.search(text):
        return False

    if PHRASE_REJECT_REL_CLAUSE.search(text):
        return False

    if PHRASE_REJECT_AUX_CHAIN.search(text):
        return False

    if PHRASE_REJECT_SLASH.search(text):
        return False

    if _JUNK_RE.search(text):
        return False

    # Reject if more than half the words are stopwords
    words = text.lower().split()
    stopwords = {"a", "an", "the", "of", "in", "to", "for", "by", "on",
                 "at", "from", "with", "about", "and", "or", "is", "are",
                 "was", "were", "be", "been", "being", "its", "it", "this",
                 "that", "these", "those"}
    if len(words) > 1 and sum(1 for w in words if w in stopwords) / len(words) > 0.6:
        return False

    return True


# ── Confidence scoring ─────────────────────────────────────────────────────────

def _confidence_score(s, p, o):
    score = 0
    s_words = s.split()
    o_words = o.split()

    if s_words and s_words[0][0].isupper():
        score += CONFIDENCE_WEIGHTS["subject_capitalized"]
    if o_words and o_words[0][0].isupper():
        score += CONFIDENCE_WEIGHTS["object_capitalized"]

    if _SPECIFIC_DOMAIN_RE.search(s):
        score += CONFIDENCE_WEIGHTS["subject_domain_specific"]
    if _SPECIFIC_DOMAIN_RE.search(o):
        score += CONFIDENCE_WEIGHTS["object_domain_specific"]

    if p.lower() in _GOOD_VERBS:
        score += CONFIDENCE_WEIGHTS["verb_in_good_verbs"]

    if len(s_words) >= 2:
        score += CONFIDENCE_WEIGHTS["subject_multiword"]
    if len(o_words) >= 2:
        score += CONFIDENCE_WEIGHTS["object_multiword"]

    if _CAMEL_RE.search(s):
        score += CONFIDENCE_WEIGHTS["subject_has_camelcase"]
    if _CAMEL_RE.search(o):
        score += CONFIDENCE_WEIGHTS["object_has_camelcase"]

    if _XAMZ_RE.search(s):
        score += CONFIDENCE_WEIGHTS["subject_xamz"]

    return score


# ── Copula validation ──────────────────────────────────────────────────────────

def _copula_is_strong(s, o):
    """
    Accept a copula triple only if the object head is a strong definitional noun
    and neither entity is generic/weak.
    """
    o_head = o.lower().split()[-1] if o.split() else ""
    s_head = s.lower().split()[-1] if s.split() else ""

    if o_head not in COPULA_STRONG_HEADS:
        return False

    # Reject "X IS supported/required/valid/optional"
    weak_adj = {"supported", "required", "valid", "optional", "available",
                "deprecated", "enabled", "disabled", "recommended", "allowed"}
    if o_head in weak_adj:
        return False

    if s_head in _GENERIC_HEAD_NOUNS:
        return False

    # Object must have at least two words to be definitional
    if len(o.split()) < 2:
        return False

    return True


# ── Dependency matcher ─────────────────────────────────────────────────────────

def _build_matcher():
    m = DependencyMatcher(NLP.vocab)

    m.add("SVO", [[
        {"RIGHT_ID": "v", "RIGHT_ATTRS": {"POS": "VERB"}},
        {"LEFT_ID": "v", "REL_OP": ">", "RIGHT_ID": "s",
         "RIGHT_ATTRS": {"DEP": {"IN": ["nsubj", "nsubjpass"]}}},
        {"LEFT_ID": "v", "REL_OP": ">", "RIGHT_ID": "o",
         "RIGHT_ATTRS": {"DEP": {"IN": ["dobj", "oprd"]}}},
    ]])

    m.add("COPULA", [[
        {"RIGHT_ID": "c", "RIGHT_ATTRS": {"LEMMA": {"IN": list(_COPULA_LEMMAS)}}},
        {"LEFT_ID": "c", "REL_OP": ">", "RIGHT_ID": "s",
         "RIGHT_ATTRS": {"DEP": "nsubj"}},
        {"LEFT_ID": "c", "REL_OP": ">", "RIGHT_ID": "o",
         "RIGHT_ATTRS": {"DEP": "attr"}},
    ]])

    m.add("POBJ", [[
        {"RIGHT_ID": "v", "RIGHT_ATTRS": {"POS": "VERB"}},
        {"LEFT_ID": "v", "REL_OP": ">", "RIGHT_ID": "s",
         "RIGHT_ATTRS": {"DEP": {"IN": ["nsubj", "nsubjpass"]}}},
        {"LEFT_ID": "v", "REL_OP": ">", "RIGHT_ID": "p",
         "RIGHT_ATTRS": {"DEP": "prep"}},
        {"LEFT_ID": "p", "REL_OP": ">", "RIGHT_ID": "o",
         "RIGHT_ATTRS": {"DEP": "pobj"}},
    ]])

    return m


_MATCHER = _build_matcher()


def _normalize_predicate(raw):
    if not raw:
        return None
    if raw.upper() in {"IS", "ARE", "BE", "WAS", "WERE"}:
        return "IS"
    if raw.upper() in {"HAS", "HAVE"}:
        return "HAS"
    if "_" in raw:
        verb = raw.split("_")[0]
        verb = VERB_NORMALIZATION.get(verb.lower(), verb.lower())
        return _VERB_MAP.get(verb, verb.upper())
    v = VERB_NORMALIZATION.get(raw.lower(), raw.lower())
    return _VERB_MAP.get(v, v.upper())


def _head_noun(text):
    words = text.lower().split()
    return words[-1] if words else ""


def _has_capitalized_term(text):
    return any(w[0].isupper() and len(w) > 1 for w in text.split())


def _has_meaningful_noun(text):
    words = text.lower().split()
    return any(
        w not in _GENERIC_OBJECT_WORDS
        and w not in _STOP_LAST
        and len(w) > 2
        for w in words
    )


def _specificity_score(s, o):
    score = 0
    score += len(s.split())
    score += len(o.split())
    if _has_capitalized_term(s):
        score += 3
    if _has_capitalized_term(o):
        score += 3
    return score


def _valid_entity(text):
    if not text:
        return False
    low = text.lower().strip()
    if low in _INVALID_ENTITIES:
        return False
    if _JUNK_RE.search(text):
        return False
    first_word = low.split()[0] if low.split() else ""
    if first_word in _LEADING_PREPS:
        return False
    if re.match(r"^\d+$", text.strip()):
        return False
    text = re.sub(r"^(a|an|the|this|that|these|those)\s+", "", text, flags=re.I).strip()
    if len(text) < 2:
        return False
    if _head_noun(text) in _GENERIC_HEAD_NOUNS:
        return False
    return text


def _valid_object(text):
    if not text:
        return False
    if _JUNK_RE.search(text):
        return False
    words = text.lower().split()
    if len(words) < 2:
        return False
    if words[-1] in _STOP_LAST:
        return False
    stripped = re.sub(r"^(a|an|the|this|that|these|those)\s+", "", text, flags=re.I).strip().lower()
    if stripped in _GENERIC_OBJECT_WORDS:
        return False
    if not _has_meaningful_noun(text):
        return False
    return True


def _shares_root(s, o):
    s_root = _head_noun(s)
    o_root = _head_noun(o)
    return s_root and o_root and (s_root == o_root or s_root in o_root or o_root in s_root)


def _both_weak(s, o, v):
    weak_predicates = {"USES", "HAS", "IS", "PROVIDES", "CONTAINS", "INCLUDES"}
    s_generic = _head_noun(s) in _GENERIC_HEAD_NOUNS or s.lower() in _GENERIC_OBJECT_WORDS
    o_generic = _head_noun(o) in _GENERIC_HEAD_NOUNS or o.lower() in _GENERIC_OBJECT_WORDS
    return v in weak_predicates and s_generic and o_generic


def _bad_subject(s):
    low = s.lower()
    words = low.split()

    if not words:
        return True

    if words[0] in {"following", "this", "that"}:
        return True

    if any(w in _NARRATIVE_TOKENS for w in words):
        return True

    if len(words) <= 2 and words[-1] in _GENERIC_SHORT_SUBJECTS:
        return True

    return False


def _bad_object(o):
    low = o.lower()
    words = low.split()

    if len(words) < 2:
        return True

    if any(w in _NARRATIVE_OBJECT_PHRASES for w in words):
        return True

    stripped = re.sub(r"^(a|an|the|this|that|these|those)\s+", "", low).strip()
    stripped_words = stripped.split()
    if stripped_words and stripped_words[0] in _NARRATIVE_OBJECT_PHRASES:
        return True

    return False


def _not_domain_relevant(s, o):
    return not _has_capitalized_term(s) and not _has_capitalized_term(o)


# ── Core extraction ────────────────────────────────────────────────────────────

def extract_raw(doc):
    triples = []
    seen = set()

    for match_id, ids in _MATCHER(doc):
        name = doc.vocab.strings[match_id]
        try:
            if name == "SVO":
                v, s, o = (doc[i] for i in ids)

                # Sentence-level gate
                sent_text = s.sent.text if s.sent else ""
                if not _sentence_is_clean(sent_text):
                    continue

                subj = _extract_np(s)
                pred = v.lemma_
                obj = _extract_np(o)

            elif name == "COPULA":
                c, s, o = (doc[i] for i in ids)

                sent_text = s.sent.text if s.sent else ""
                if not _sentence_is_clean(sent_text):
                    continue

                subj = _extract_np(s)
                pred = "IS"
                obj = _extract_np(o)

                # Restrict copulas to definitional ones only
                if not _copula_is_strong(subj, obj):
                    continue

            elif name == "POBJ":
                v, s, p, o = (doc[i] for i in ids)

                sent_text = s.sent.text if s.sent else ""
                if not _sentence_is_clean(sent_text):
                    continue

                subj = _extract_np(s)
                pred = v.lemma_
                obj = _extract_np(o)

            else:
                continue

        except Exception:
            continue

        # Phrase-level structural check
        if not _phrase_is_clean(subj) or not _phrase_is_clean(obj):
            continue

        key = (subj.lower(), pred.lower(), obj.lower())
        if key in seen:
            continue
        seen.add(key)

        triples.append({"s": subj, "p": pred, "o": obj})

    return triples


def clean_akus(raw):
    out = []
    seen = set()

    for t in raw:
        s = _valid_entity(t["s"])
        o = t["o"]
        p = _normalize_predicate(t["p"])

        if not s or not p:
            continue
        if not _valid_object(o):
            continue

        o_clean = re.sub(r"^(a|an|the|this|that|these|those)\s+", "", o, flags=re.I).strip()
        if not o_clean:
            continue

        if s.lower() == o_clean.lower():
            continue

        if _shares_root(s, o_clean):
            continue

        if _both_weak(s, o_clean, p):
            continue

        if _bad_subject(s):
            continue

        if _bad_object(o_clean):
            continue

        if _not_domain_relevant(s, o_clean):
            continue

        # Phrase structural checks post-entity-validation
        if not _phrase_is_clean(s) or not _phrase_is_clean(o_clean):
            continue

        # Confidence gate
        score = _confidence_score(s, p, o_clean)
        if score < CONFIDENCE_THRESHOLD:
            continue

        key = (s.lower(), p, o_clean.lower())
        if key in seen:
            continue
        seen.add(key)

        out.append((score, [s, p, o_clean]))

    # Sort by confidence descending, then by phrase specificity as tiebreaker
    out.sort(key=lambda x: (x[0], _specificity_score(x[1][0], x[1][2])), reverse=True)
    return [aku for _, aku in out[:MAX_AKUS]]


def extract_akus_from_chunk(chunk, doc=None):
    meta = chunk.get("metadata", {})
    text = chunk.get("content", "").strip()
    chunk_id = meta.get("chunk_id", "")

    if not text:
        return {"chunk_id": chunk_id, "akus": []}

    if doc is None:
        doc = NLP(text)

    raw = extract_raw(doc)
    akus = clean_akus(raw)

    return {"chunk_id": chunk_id, "akus": akus}


def extract_akus_batch(chunks):
    texts = [c.get("content", "") for c in chunks]
    docs = list(NLP.pipe(texts, batch_size=AKU_BATCH_SIZE))

    out = []
    for c, d in zip(chunks, docs):
        r = extract_akus_from_chunk(c, doc=d)
        if r["akus"]:
            out.append(r)

    print(f"[AKU] {len(chunks)} → {len(out)}")
    return out
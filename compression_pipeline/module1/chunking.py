import re
import numpy as np
from sentence_transformers import SentenceTransformer

from constants import (
    SENT_NLP,
    TOKENIZER,
    MIN_SENT_WORDS,
    MAX_SENT_WORDS,
    MIN_CHUNK_TOKENS,
    TARGET_CHUNK_TOKENS,
    MAX_CHUNK_TOKENS,
    OVERLAP_TOKENS,
    WORD_RE,
)

from aku import is_code_noise, is_domain_phrase

# ----------------------------
# MODEL (lazy load for perf)
# ----------------------------
_EMBED_MODEL = None


def get_embed_model():
    global _EMBED_MODEL
    if _EMBED_MODEL is None:
        _EMBED_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
    return _EMBED_MODEL


# ----------------------------
# TOKEN UTILITIES
# ----------------------------
def word_count(text):
    return len(WORD_RE.findall(text))


def token_count(text):
    return len(TOKENIZER.encode(text))


def token_overlap(text, n_tokens=OVERLAP_TOKENS):
    tokens = TOKENIZER.encode(text)
    return TOKENIZER.decode(tokens[-n_tokens:])


# ----------------------------
# SENTENCE PROCESSING
# ----------------------------
def split_sentences(text):
    doc = SENT_NLP(text)
    return [s.text.strip() for s in doc.sents if s.text.strip()]


def valid_sentence(sentence):
    if sentence.startswith(("•", "-", "*")):
        return False

    words = word_count(sentence)

    if words < MIN_SENT_WORDS:
        return False

    if words > MAX_SENT_WORDS * 2:
        return False

    if is_code_noise(sentence) and not is_domain_phrase(sentence):
        return False

    if sentence.lower().startswith(
        ("for more information", "the following", "this example")
    ):
        return False

    return True


def split_long_sentence(sentence):
    words = sentence.split()

    if len(words) <= MAX_SENT_WORDS:
        return [sentence]

    parts = []
    for i in range(0, len(words), MAX_SENT_WORDS):
        part = " ".join(words[i : i + MAX_SENT_WORDS]).strip()
        if word_count(part) >= MIN_SENT_WORDS:
            parts.append(part)

    return parts


# ----------------------------
# SEMANTIC GROUPING
# ----------------------------
def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def group_sentences_semantically(sentences):
    if not sentences:
        return []

    model = get_embed_model()
    embeddings = model.encode(sentences)

    groups = []
    current_group = [sentences[0]]
    current_emb = embeddings[0]

    for i in range(1, len(sentences)):
        sim = cosine_sim(current_emb, embeddings[i])

        # stricter threshold → better coherence
        if sim >= 0.7:
            current_group.append(sentences[i])
            current_emb = (current_emb + embeddings[i]) / 2
        else:
            groups.append(current_group)
            current_group = [sentences[i]]
            current_emb = embeddings[i]

    groups.append(current_group)
    return groups


# ----------------------------
# CHUNK BUILDING
# ----------------------------
def build_chunks(sections):
    chunks = []
    cid = 0

    for section in sections:
        text = clean_text(section["content"])

        # ---- sentence extraction ----
        raw_sentences = []
        for sentence in split_sentences(text):
            if valid_sentence(sentence):
                raw_sentences.extend(split_long_sentence(sentence))

        if not raw_sentences:
            continue

        # ---- semantic grouping ----
        sentence_groups = group_sentences_semantically(raw_sentences)

        # ---- token packing ----
        cur = []
        cur_tokens = 0

        for group in sentence_groups:
            group_text = " ".join(group)
            group_tokens = token_count(group_text)

            # overflow → flush
            if cur and cur_tokens + group_tokens > MAX_CHUNK_TOKENS:
                cid = append_chunk(chunks, cur, section, cid)
                cur = []
                cur_tokens = 0

            cur.append(group_text)
            cur_tokens += group_tokens

            # target reached → flush
            if cur_tokens >= TARGET_CHUNK_TOKENS:
                cid = append_chunk(chunks, cur, section, cid)
                cur = []
                cur_tokens = 0

        # final flush
        if cur:
            cid = append_chunk(chunks, cur, section, cid)

    apply_overlap(chunks)
    return chunks


# ----------------------------
# CHUNK APPEND
# ----------------------------
def append_chunk(chunks, sentences, section, cid):
    text = " ".join(sentences)
    tokens = token_count(text)

    # merge small chunks instead of dropping
    if tokens < MIN_CHUNK_TOKENS:
        if chunks:
            chunks[-1]["text"] += " " + text
            chunks[-1]["tokens"] = token_count(chunks[-1]["text"])
        return cid

    chunks.append(
        {
            "chunk_id": f"c{cid}",
            "text": text,
            "tokens": tokens,
            "heading_path": section["heading_path"],
            "section_id": section["section_id"],
            "source": section.get("source", "unknown"),
            "position": cid,
        }
    )

    return cid + 1


# ----------------------------
# OVERLAP
# ----------------------------
def apply_overlap(chunks):
    for i in range(1, len(chunks)):
        if len(chunks[i]["text"]) < 50:
            continue

        overlap = token_overlap(chunks[i - 1]["text"])
        chunks[i]["text"] = overlap + " " + chunks[i]["text"]
        chunks[i]["tokens"] = token_count(chunks[i]["text"])


# ----------------------------
# CLEANING
# ----------------------------
def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\bNote\b.*?\.", " ", text)
    text = re.sub(r"\bImportant\b.*?\.", " ", text)
    text = re.sub(
        r"\b(?:Request|Response) Headers?\b.*?(?=\b[A-Z][A-Za-z ]{3,}\b|$)",
        " ",
        text,
    )
    return text.strip()
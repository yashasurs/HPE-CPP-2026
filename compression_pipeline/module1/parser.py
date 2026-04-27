import os, re, json, uuid, unicodedata
import spacy
from markdown_it import MarkdownIt

# ==============================
# MODEL
# ==============================
nlp = spacy.load("en_core_web_trf")

# ==============================
# GLOBAL DEDUP
# ==============================
GLOBAL_SEEN = set()

# ==============================
# FILTER RULES
# ==============================
BAD_SUBJECTS = {
    "you","we","it","they","this","that","who","which",
    "the service","the request","this request","the response",
    "this response","this section","the following","example",
    "request","name","value","data"
}

BAD_OBJECTS = {
    "value","data","object","thing","information","example",
    "parameter","request","response"
}

BAD_VERBS = {
    "be","have","do","make","use","is","are","was","were",
    "has","had","can","could","will","would","should","may","might",
    "set","get","list","create","delete",
    "see","include","contain","show","provide"
}

DOMAIN_TERMS = {
    "aws","s3","bucket","object","header","request","response",
    "encryption","kms","policy","api","endpoint","session","checksum"
}

# ==============================
# CLEANING
# ==============================
def clean_phrase(t):
    t = unicodedata.normalize("NFKD", t)

    t = re.sub(r"(Amazon S3 ){2,}", "Amazon S3 ", t)
    t = re.sub(r"(Amazon Simple Storage Service.*)", "", t)

    return t.strip()

def load_md(p):
    text = open(p, "r", encoding="utf-8").read()
    text = re.sub(r".*\.{10,}.*\n","",text)
    text = re.sub(r"API Version \d{4}-\d{2}-\d{2}.*\n","",text)
    text = re.sub(r"Copyright.*\n","",text)
    text = re.sub(r"Amazon's trademarks.*\n","",text)
    text = unicodedata.normalize("NFKD", text)
    return text

# ==============================
# PARSER
# ==============================
def parse_md(text):
    md = MarkdownIt()
    tokens = md.parse(text)

    sections, stack = [], []
    current = {"heading_path": [], "content": [], "section_id": str(uuid.uuid4())}

    i = 0
    while i < len(tokens):
        t = tokens[i]

        if t.type == "heading_open":
            level = int(t.tag[1])
            title = tokens[i+1].content.strip()

            if current["content"]:
                sections.append({
                    "section_id": current["section_id"],
                    "heading_path": current["heading_path"],
                    "content": " ".join(current["content"])
                })

            current = {
                "heading_path": stack[:level-1] + [title],
                "content": [],
                "section_id": str(uuid.uuid4())
            }

            stack = stack[:level-1] + [title]
            i += 2

        elif t.type == "paragraph_open":
            current["content"].append(tokens[i+1].content.strip())
            i += 2

        elif t.type == "inline" and t.content.strip():
            current["content"].append(t.content.strip())
            i += 1

        elif t.type == "bullet_list_open":
            items = []
            i += 1
            while tokens[i].type != "bullet_list_close":
                if tokens[i].type == "inline":
                    items.append(tokens[i].content.strip())
                i += 1
            current["content"].append(" ".join(items))
            i += 1

        else:
            i += 1

    if current["content"]:
        sections.append({
            "section_id": current["section_id"],
            "heading_path": current["heading_path"],
            "content": " ".join(current["content"])
        })

    return sections

# ==============================
# TEXT PROCESSING
# ==============================
def clean_text(t):
    t = re.sub(r"\s+"," ",t)
    t = re.sub(r"Note .*?\.","",t)
    t = re.sub(r"Important .*?\.","",t)
    return t.strip()

def split_sentences(t):
    return re.split(r'(?<=[.!?])\s+', t)

def valid_sentence(s):
    w = s.split()
    return 8 <= len(w) <= 40 and not s.startswith(("•","-","*"))

# ==============================
# CHUNKING
# ==============================
def build_chunks(sections):
    chunks, cid = [], 0

    for sec in sections:
        text = clean_text(sec["content"])
        sents = [s for s in split_sentences(text) if valid_sentence(s)]

        cur = []
        for s in sents:
            cur.append(s)

            if len(" ".join(cur).split()) > 500:
                chunk = " ".join(cur)
                if len(chunk.split()) >= 200:
                    chunks.append(make_chunk(chunk, sec, cid))
                    cid += 1
                cur = []

        if cur:
            chunk = " ".join(cur)
            if len(chunk.split()) >= 200:
                chunks.append(make_chunk(chunk, sec, cid))
                cid += 1

    return chunks

def make_chunk(text, sec, cid):
    return {
        "chunk_id": f"c{cid}",
        "text": text,
        "tokens": len(text.split()),
        "heading_path": sec["heading_path"],
        "section_id": sec["section_id"]
    }

# ==============================
# FILTER HELPERS
# ==============================
def is_domain_phrase(t):
    return any(d in t.lower() for d in DOMAIN_TERMS)

def is_weak_subject(s):
    return any(s.lower().startswith(x) for x in [
        "this","that","these","those","it",
        "the request","the operation","the command","the following"
    ])

def is_code_noise(t):
    return bool(re.search(r"[=(){}$]|::|->|client|sdk|new |const |class ", t.lower()))

def is_http_noise(t):
    return any(x in t.lower() for x in [
        "http","status","response","error","code",
        "ok","not found","denied","success"
    ])

def is_bad_phrase(t):
    t = t.lower()
    return any(x in t for x in ["type","required","valid values","example","contents"])

def is_incomplete(o):
    return (
        len(o.split()) < 3 or
        o.strip().endswith(("the","a","an","of","to","with","for","in","by","and","or"))
    )

# ==============================
# SCORING
# ==============================
def score_aku(s, v, o):
    score = 0

    if is_domain_phrase(s): score += 2
    if is_domain_phrase(o): score += 2

    if v not in BAD_VERBS: score += 1

    if 2 <= len(s.split()) <= 5: score += 1
    if 3 <= len(o.split()) <= 7: score += 1

    if is_code_noise(s) or is_code_noise(o): score -= 5
    if is_http_noise(o): score -= 4
    if is_incomplete(o): score -= 3
    if is_weak_subject(s): score -= 4
    if is_bad_phrase(s): score -= 3

    return score

def valid_aku(s, v, o):
    s, o = clean_phrase(s), clean_phrase(o)

    s_l, o_l = s.lower(), o.lower()

    if s_l in BAD_SUBJECTS or o_l in BAD_OBJECTS:
        return False

    if v in BAD_VERBS:
        return False

    if len(s.split()) < 2:
        return False

    if is_weak_subject(s):
        return False

    if is_code_noise(s) or is_code_noise(o):
        return False

    if is_http_noise(o):
        return False

    if is_incomplete(o):
        return False

    if is_bad_phrase(s):
        return False

    return score_aku(s, v, o) >= 4

# ==============================
# AKU EXTRACTION
# ==============================
def expand_np(tok):
    return " ".join([t.text for t in tok.subtree if not t.is_punct][:7])

def extract_akus_batch(chunks):
    texts = [c["text"] for c in chunks]
    docs = list(nlp.pipe(texts, batch_size=8))

    results = []

    for i, doc in enumerate(docs):
        akus = []

        for sent in doc.sents:
            for tok in sent:
                if tok.pos_ == "VERB":
                    subs, objs = [], []

                    for c in tok.children:
                        if c.dep_ in ("nsubj","nsubjpass"):
                            subs.append(expand_np(c))
                        if c.dep_ in ("dobj","pobj","attr"):
                            objs.append(expand_np(c))

                    for s in subs:
                        for o in objs:
                            if valid_aku(s, tok.lemma_, o):
                                key = tuple([s.lower(), tok.lemma_, o.lower()])
                                if key not in GLOBAL_SEEN:
                                    GLOBAL_SEEN.add(key)
                                    akus.append([clean_phrase(s), tok.lemma_, clean_phrase(o)])

        clean = sorted(akus, key=lambda x: score_aku(*x), reverse=True)[:5]

        results.append({
            "chunk_id": chunks[i]["chunk_id"],
            "akus": clean
        })

    return results

# ==============================
# MAIN
# ==============================
def run(input_path, output_dir):
    raw = load_md(input_path)
    sections = parse_md(raw)
    chunks = build_chunks(sections)

    for i in range(1, len(chunks)):
        prev = chunks[i-1]["text"].split()
        overlap = " ".join(prev[-80:])
        chunks[i]["text"] = overlap + " " + chunks[i]["text"]

    akus = extract_akus_batch(chunks)
    akus = [a for a in akus if a["akus"]]

    os.makedirs(output_dir, exist_ok=True)
    json.dump(chunks, open(os.path.join(output_dir,"chunks.json"),"w"), indent=2)
    json.dump(akus, open(os.path.join(output_dir,"akus.json"),"w"), indent=2)

    print(f"Done | Chunks: {len(chunks)} | AKUs: {sum(len(a['akus']) for a in akus)}")

# ==============================
# ENTRY
# ==============================
if __name__ == "__main__":
    run("../../data/prototype/S3/L0/s3-api.md","s3/intermediate")
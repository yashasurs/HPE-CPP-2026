import argparse
import json
import os
import re
import unicodedata
import uuid

from markdown_it import MarkdownIt
from constants import NOISE_PATTERNS, LOW_VALUE_SECTION_TITLES
from chunking import build_chunks
from aku import extract_akus_batch


def normalize_text(text):
    return unicodedata.normalize("NFKD", text)


def load_md(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    text = normalize_text(text)
    for pattern in NOISE_PATTERNS:
        text = pattern.sub("", text)

    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"\bFor more information,?\s+see\b[^.]*\.", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"\b(?:GET|PUT|POST|DELETE|HEAD|OPTIONS)\s+[^\n]+?\s+HTTP/[0-9.]+", " ", text)
    text = re.sub(r"\b[A-Fa-f0-9]{24,}\b", " ", text)
    text = re.sub(r"\b[A-Z0-9+/]{24,}={0,2}\b", " ", text)
    return text



def parse_md(text):
    md = MarkdownIt()
    tokens = md.parse(text)

    sections = []
    stack = []
    current = new_section([])

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.type == "heading_open":
            level = int(token.tag[1])
            title = tokens[i + 1].content.strip()
            flush_section(sections, current)

            stack = stack[:level - 1] + [title]
            current = new_section(stack)
            i += 2
            continue

        if token.type == "inline" and token.content.strip():
            if not is_low_value_heading(current["heading_path"]):
                current["content"].append(token.content.strip())
            i += 1
            continue

        i += 1

    flush_section(sections, current)
    return sections


def new_section(heading_path):
    return {
        "section_id": str(uuid.uuid4()),
        "heading_path": list(heading_path),
        "content": [],
    }


def flush_section(sections, section):
    from chunking import word_count
    
    if not section["content"]:
        return

    content = " ".join(section["content"])
    if word_count(content) < 40:
        return

    sections.append({
        "section_id": section["section_id"],
        "heading_path": section["heading_path"],
        "content": content,
    })


def is_low_value_heading(heading_path):
    if not heading_path:
        return False
    return heading_path[-1].strip().lower() in LOW_VALUE_SECTION_TITLES



def run(input_path, output_dir):
    raw = load_md(input_path)
    sections = parse_md(raw)
    chunks = build_chunks(sections)
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "chunks.json"), "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2)
    print("chunks done")
    akus = extract_akus_batch(chunks)

    

    with open(os.path.join(output_dir, "akus.json"), "w", encoding="utf-8") as f:
        json.dump(akus, f, indent=2)

    print(
        f"Done | Sections: {len(sections)} | Chunks: {len(chunks)} | "
        f"AKUs: {sum(len(row['akus']) for row in akus)}"
    )


if __name__ == "__main__":
    run("../../data/prototype/S3/L0/s3-api.md", "s3/intermediate")
import json
import uuid
from pathlib import Path

import tiktoken
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

from config import (
    MARKDOWN_HEADERS, CHUNK_SIZE, CHUNK_OVERLAP,
    MIN_TOKEN_COUNT
)

_ENCODER = tiktoken.encoding_for_model("gpt-3.5-turbo")

def count_tokens(text: str) -> int:
    return len(_ENCODER.encode(text))


def normalize_markdown(text: str) -> str:
    lines = text.split("\n")
    out = []
    for line in lines:
        stripped = line.strip()
        if (
            stripped
            and not stripped.startswith("#")
            and (stripped.endswith("Upload") or "Multipart" in stripped)
            and len(stripped.split()) < 10
        ):
            out.append(f"### {stripped}")
            continue
        if stripped.startswith("#"):
            content = stripped.lstrip("#").strip()
            if content.startswith(("$", "@", "-", "*", "•")) or len(content.split()) > 15:
                out.append(content)
                continue

        out.append(line)
        
    return "\n".join(out)


def chunk_document(text: str, source_doc: str) -> list[dict]:
    text = normalize_markdown(text)

    header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=MARKDOWN_HEADERS, strip_headers=False
    )
    header_chunks = header_splitter.split_text(text)

    char_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        model_name="gpt-3.5-turbo",
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["```", "\n\n", "\n", ". ", " ", ""],
        keep_separator=True,
    )

    final_chunks = char_splitter.split_documents(header_chunks)

    output = []

    for i, chunk in enumerate(final_chunks):
        m = chunk.metadata
        heading_path = [m[h] for _, h in MARKDOWN_HEADERS if m.get(h)]
        token_count = count_tokens(chunk.page_content)

        if token_count < MIN_TOKEN_COUNT:
            continue

        output.append(
            {
                "metadata": {
                    "chunk_id": str(uuid.uuid4()),
                    "source_doc": source_doc,
                    "position": i,
                    "heading_path": heading_path,
                    "knowledge_category": "Factual",
                    "token_count": token_count,
                },
                "content": chunk.page_content,
                "aku_hints": [],
            }
        )

    print(f"[CHUNKS] count: {len(output)}")
    return output

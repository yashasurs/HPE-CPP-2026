import argparse, json, sys, uuid
from pathlib import Path
import tiktoken
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

HEADERS = [("#", "H1"), ("##", "H2"), ("###", "H3")]
CHUNK_SIZE = 1000
OVERLAP = 100

enc = tiktoken.encoding_for_model("gpt-3.5-turbo")


def count_tokens(text: str) -> int:
    return len(enc.encode(text))


def normalize_markdown(text: str) -> str:
    lines = text.split("\n")
    out = []
    for line in lines:
        if (
            line.strip()
            and not line.startswith("#")
            and line.strip().endswith("Upload")
            or "Multipart" in line
        ):
            out.append(f"### {line.strip()}")
        else:
            out.append(line)
    return "\n".join(out)


def chunk_document(text: str, source_doc: str) -> list[dict]:
    text = normalize_markdown(text)

    header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=HEADERS, strip_headers=False
    )
    header_chunks = header_splitter.split_text(text)

    char_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        model_name="gpt-3.5-turbo",
        chunk_size=CHUNK_SIZE,
        chunk_overlap=OVERLAP,
        separators=["```", "\n\n", "\n", ". ", " ", ""],
        keep_separator=True,
    )

    final_chunks = char_splitter.split_documents(header_chunks)

    output = []
    prev_tokens = 0

    for i, chunk in enumerate(final_chunks):
        m = chunk.metadata
        heading_path = [m[h] for _, h in HEADERS if m.get(h)]
        token_count = count_tokens(chunk.page_content)

        if token_count < 75:
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

        prev_tokens = token_count

    return output


def main():
    p = argparse.ArgumentParser()
    p.add_argument("input_file")
    p.add_argument("-o", "--output", default="chunks.json")
    a = p.parse_args()

    path = Path(a.input_file)
    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(1)

    text = path.read_text(encoding="utf-8")
    chunks = chunk_document(text, str(path))

    print(len(chunks))
    Path(a.output).write_text(
        json.dumps(chunks, indent=2, ensure_ascii=False), encoding="utf-8"
    )


if __name__ == "__main__":
    main()

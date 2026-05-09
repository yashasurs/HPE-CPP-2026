import argparse
import json
from pathlib import Path

from parser.cleaner import clean_markdown
from chunking.chunker import chunk_document
from aku.aku import extract_akus_batch


def validate_chunks(chunks):
    for c in chunks:
        if "metadata" not in c or "content" not in c:
            raise ValueError("Invalid chunk format: missing metadata/content")


def save_output(path, data):
    Path(path).write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


def run(input_file: str, output_dir: str) -> None:
    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    raw_text = input_path.read_text(encoding="utf-8")

    cleaned_text = clean_markdown(raw_text)
    cleaned_path = out_dir / f"{input_path.stem}.cleaned.md"
    cleaned_path.write_text(cleaned_text, encoding="utf-8")

    chunks = chunk_document(cleaned_text, str(input_path))
    validate_chunks(chunks)

    chunks_path = out_dir / "chunks.json"
    save_output(chunks_path, chunks)

    aku_input = [
        {
            "metadata": chunk["metadata"],
            "content": chunk["content"]
        }
        for chunk in chunks
    ]

    akus = extract_akus_batch(aku_input)

    akus_path = out_dir / "akus.json"
    save_output(akus_path, akus)

    total_akus = sum(len(row.get("akus", [])) for row in akus)

    print(f"Cleaned: {cleaned_path}")
    print(f"Chunks:  {chunks_path} ({len(chunks)} chunks)")
    print(f"AKUs:    {akus_path} ({total_akus} akus across {len(akus)} chunks)")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run pipeline: cleaner -> chunker -> AKU extraction"
    )
    parser.add_argument(
        "input_file",
        nargs="?",
        default="data/prototype/S3/L0/s3-api.md",
        help="Path to input markdown file",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default="compression_pipeline/module1/s3/intermediate",
        help="Directory to write outputs",
    )

    args = parser.parse_args()
    run(args.input_file, args.output_dir)


if __name__ == "__main__":
    main()
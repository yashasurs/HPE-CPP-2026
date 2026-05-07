import re
from pathlib import Path
from config import (
    NOISE_PATTERNS, REPEATED_LINE_THRESHOLD, TECHNICAL_PATTERNS,
    TECHNICAL_PREFIXES, ENCODING_FIXES
)

def protect_code_blocks(text):
    mapping = {}
    counter = 0

    def replacer(match):
        nonlocal counter
        key = f"__CODE_BLOCK_{counter}__"
        mapping[key] = match.group(0)
        counter += 1
        return key

    text = re.sub(r"```.*?```", replacer, text, flags=re.DOTALL)
    return text, mapping


def restore_code_blocks(text, mapping):
    for k, v in mapping.items():
        text = text.replace(k, v)
    return text


def fix_encoding(text):
    for k, v in ENCODING_FIXES.items():
        text = text.replace(k, v)
    return text


def remove_noise_lines(lines):
    cleaned = []

    for line in lines:
        l = line.strip()

        if not l:
            continue

        if any(re.search(p, l, re.IGNORECASE) for p in NOISE_PATTERNS):
            continue

        # remove breadcrumbs like A > B > C
        if ">" in l and len(l.split(">")) >= 3:
            continue

        cleaned.append(line)

    return cleaned


def remove_repeated_lines(lines):
    freq = {}
    for l in lines:
        key = l.strip()
        freq[key] = freq.get(key, 0) + 1

    cleaned = []
    for l in lines:
        if freq[l.strip()] > REPEATED_LINE_THRESHOLD:
            continue
        cleaned.append(l)

    return cleaned


def remove_toc_blocks(text):
    text = re.sub(r".*\.{5,}.*\n", "", text)
    text = re.sub(r"(\n[\-\*\•].*){10,}", "", text)
    return text


def remove_legal_blocks(text):
    lines = text.split("\n")
    cleaned = []

    skip = False

    for line in lines:
        l = line.lower()

        if "confusion among customers" in l:
            skip = True
            continue

        if skip:
            # stop skipping after blank or heading
            if not l.strip() or l.startswith("#"):
                skip = False
            continue

        cleaned.append(line)

    return "\n".join(cleaned)


def clean_links(text):
    return re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)


def remove_urls(text):
    return re.sub(r"https?://\S+", "", text)


def normalize_bullets(text):
    return re.sub(r"^\s*[-\*\•]\s+(.*)", r"\1.", text, flags=re.MULTILINE)





def fix_punctuation(text):
    text = re.sub(r"\s+\.", ".", text)
    text = re.sub(r"\.{2,}", ".", text)
    text = re.sub(r"\s+,", ",", text)
    return text


def remove_junk(text):
    text = re.sub(r"\?{2,}", "", text)
    text = re.sub(r"[^\w\s\.\,\-\(\)\/:]+$", "", text, flags=re.MULTILINE)
    return text


def remove_short_fragments(text):
    lines = text.split("\n")
    cleaned = []

    for l in lines:
        if len(l.strip()) < 3:
            continue
        cleaned.append(l)

    return "\n".join(cleaned)


def fix_heading_noise(text):
    return re.sub(r"(## .+)\n([A-Za-z]{1,10})\n", r"\1\n", text)


def normalize_spacing(text):
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def remove_orphan_lines(text):
    lines = text.split("\n")
    cleaned = []
    for l in lines:
        s = l.strip()
        if (
            len(s) < 25
            and not s.startswith("#")
            and not is_api_line(s)
            and not TECHNICAL_PATTERNS.match(s)
            and not s.startswith("x-amz-")
        ):
            if not s.endswith("."):
                continue
        if s.startswith("(") and len(s) < 40:
            continue
        cleaned.append(l)
    return "\n".join(cleaned)


def merge_broken_lines(text):
    lines = text.split("\n")
    merged = []
    buffer = ""

    for line in lines:
        stripped = line.strip()

        if stripped == "":
            if buffer:
                merged.append(buffer.strip())
                buffer = ""
            merged.append("")
            continue

        if is_api_line(stripped):
            if buffer:
                merged.append(buffer.strip())
                buffer = ""
            merged.append(line)
            continue

        if (
            stripped.startswith("#")
            or stripped.startswith("-")
            or stripped.startswith("*")
            or stripped.startswith(">")
            or re.match(r"^[A-Z][A-Za-z\s]{2,30}$", stripped)
            or re.match(r"^[A-Z0-9\-]+ /", stripped)
        ):
            if buffer:
                merged.append(buffer.strip())
                buffer = ""
            merged.append(line)
        else:
            if buffer:
                buffer += " " + stripped
            else:
                buffer = stripped

    if buffer:
        merged.append(buffer.strip())

    return "\n".join(merged)


def promote_section_headers(text):
    lines = text.split("\n")
    new_lines = []

    for line in lines:
        if re.match(
            r"^(Version|Actions|Data types|API call recommendations)\b", line.strip()
        ):
            new_lines.append("## " + line.strip())
        else:
            new_lines.append(line)

    return "\n".join(new_lines)


def is_api_line(line):
    return bool(re.search(r"(HTTP/1\.1|x-amz-|DELETE|PUT|POST)", line))


def remove_empty_bullets(text):
    return re.sub(r"^\s*-\s*\.\s*$", "", text, flags=re.MULTILINE)


def remove_duplicate_headers(text):
    lines = text.split("\n")
    cleaned = []
    prev = None

    for l in lines:
        if l.strip() == prev:
            continue
        cleaned.append(l)
        prev = l.strip()

    return "\n".join(cleaned)


def preview(text, n=120):
    return text[:n].replace("\n", " ")


def clean_markdown(text):
    print("\n[START] Raw text length:", len(text))
    print("[START preview]:", preview(text))

    text = fix_encoding(text)
    print("[fix_encoding] length:", len(text))
    # protect code blocks
    text, mapping = protect_code_blocks(text)
    print("[protect_code_blocks] length:", len(text), "| code blocks:", len(mapping))

    # early removals
    text = remove_legal_blocks(text)
    print("[remove_legal_blocks] length:", len(text))

    text = remove_toc_blocks(text)
    print("[remove_toc_blocks] length:", len(text))

    text = remove_urls(text)
    print("[remove_urls] length:", len(text))

    lines = text.split("\n")
    print("[split_lines] total lines:", len(lines))

    lines = remove_noise_lines(lines)
    print("[remove_noise_lines] total lines:", len(lines))

    lines = remove_repeated_lines(lines)
    print("[remove_repeated_lines] total lines:", len(lines))

    text = "\n".join(lines)
    print("[join_lines] length:", len(text))

    text = promote_section_headers(text)
    print("[promote_section_headers] length:", len(text))

    text = clean_links(text)
    print("[clean_links] length:", len(text))

    text = normalize_bullets(text)
    print("[normalize_bullets] length:", len(text))

    text = merge_broken_lines(text)
    print("[merge_broken_lines] length:", len(text))

    text = fix_punctuation(text)
    print("[fix_punctuation] length:", len(text))

    text = remove_orphan_lines(text)
    print("[remove_orphan_lines] length:", len(text))

    text = remove_empty_bullets(text)
    print("[remove_empty_bullets] length:", len(text))

    text = remove_duplicate_headers(text)
    print("[remove_duplicate_headers] length:", len(text))

    text = remove_junk(text)
    print("[remove_junk] length:", len(text))

    text = remove_short_fragments(text)
    print("[remove_short_fragments] length:", len(text))

    text = fix_heading_noise(text)
    print("[fix_heading_noise] length:", len(text))

    text = normalize_spacing(text)
    print("[normalize_spacing] length:", len(text))

    # restore code blocks
    text = restore_code_blocks(text, mapping)
    print("[restore_code_blocks] length:", len(text))

    print("[END] Final cleaned length:", len(text))

    return text

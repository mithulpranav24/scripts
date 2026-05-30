"""
PDF Page Extractor
Usage:
    python extract_pages.py input.pdf "1,2,4-6,8,10-12" [output.pdf]

If output.pdf is not specified, it will be named:
    {original_name}_pages_{specification}.{ext}
    e.g., document_pages_1,2,4-6.pdf
"""

import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter


def parse_page_spec(spec: str):
    """
    Parse a page specification string like "1,2,4-6,8,10-12"
    Returns a sorted list of unique 1-based page numbers.
    """
    pages = set()
    for part in spec.replace(" ", "").split(","):
        if not part:
            continue
        if "-" in part and part[0] != "-":
            start, end = part.split("-", 1)
            try:
                start_idx = int(start)
                end_idx = int(end)
                if start_idx < 1 or end_idx < 1:
                    raise ValueError("Page numbers must be positive")
                pages.update(range(start_idx, end_idx + 1))
            except ValueError as e:
                raise ValueError(f"Invalid range: {part} ({e})")
        else:
            try:
                page_num = int(part)
                if page_num < 1:
                    raise ValueError("Page numbers must be positive")
                pages.add(page_num)
            except ValueError:
                raise ValueError(f"Invalid page number: {part}")
    return sorted(pages)


def extract_pages(input_path: str, page_spec: str, output_path: str = None):
    input_path = Path(input_path)
    if not input_path.exists():
        print(f"Error: File not found: {input_path}")
        sys.exit(1)

    try:
        requested_pages = parse_page_spec(page_spec)
    except ValueError as e:
        print(f"Error in page specification: {e}")
        sys.exit(1)

    reader = PdfReader(input_path)
    total_pages = len(reader.pages)

    # Validate page numbers
    invalid = [p for p in requested_pages if p > total_pages]
    if invalid:
        print(f"Error: Requested pages exceed total pages ({total_pages}): {invalid}")
        sys.exit(1)

    writer = PdfWriter()

    for page_num in requested_pages:
        writer.add_page(reader.pages[page_num - 1])

    # Determine output filename
    if output_path is None:
        stem = input_path.stem
        suffix = input_path.suffix.lower()
        safe_spec = page_spec.replace(",", "_").replace("-", "-")
        output_path = input_path.parent / f"{stem}_pages_{safe_spec}{suffix}"
    else:
        output_path = Path(output_path)

    # Write output
    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"Extracted {len(requested_pages)} page(s) → {output_path}")
    if len(requested_pages) == 1:
        print(f"   Page {requested_pages[0]}")
    else:
        print(f"   Pages: {page_spec}")


def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print(__doc__)
        sys.exit(1)

    input_pdf = sys.argv[1]
    page_spec = sys.argv[2]
    output_pdf = sys.argv[3] if len(sys.argv) == 4 else None

    extract_pages(input_pdf, page_spec, output_pdf)


if __name__ == "__main__":
    main()
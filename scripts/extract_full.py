#!/usr/bin/env python3
"""
extract_full.py

Generate the complete page-marked text store for GEB.

Requirements:
  pip install pymupdf

Usage:
  python scripts/extract_full.py path/to/GEB.pdf text/full-marked.txt

The script walks every page, extracts text with PyMuPDF, and wraps each page
in === [PDF p. N] === markers. Residual OCR noise is left visible.
"""
import sys
import fitz  # PyMuPDF

def main(pdf_path: str, out_path: str):
    doc = fitz.open(pdf_path)
    with open(out_path, "w", encoding="utf-8") as out:
        for i, page in enumerate(doc, start=1):
            out.write(f"=== [PDF p. {i}] ===\n")
            text = page.get_text("text") or ""
            out.write(text)
            out.write("\n\n")
    print(f"Wrote {doc.page_count} pages to {out_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_full.py input.pdf output.txt")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])

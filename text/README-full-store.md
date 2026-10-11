# Full Page-Marked Text Store

The complete 821-page store (`text/full-marked.txt`, ~2 MB) is **generated locally
and not committed** — it is the full text of the book, so it stays out of the
repository (`text/full-marked.txt` is listed in `.gitignore`).

## Generate it locally

```bash
pip install pymupdf
python scripts/extract_full.py path/to/GEB.pdf text/full-marked.txt
```

Every page is wrapped in a `=== [PDF p. N] ===` marker (N = 1..821), which
grounds all annotations and quotations.

## What lives in the repo

- `text/chunks/` — small sample excerpts (page-marked) illustrating the format.
- `text/units/` — unit-level reading notes.
- `text/OCR-DIFF.md` — known OCR quirks of the source PDF.

## Verify a local generation

```bash
# Exactly 821 markers, numbered 1..821 in order
grep -c '^=== \[PDF p\.' text/full-marked.txt
grep -o '^=== \[PDF p\.[0-9]*\] ===' text/full-marked.txt \
  | grep -o '[0-9]*' | awk '$1!=NR{print "GAP at",NR; bad=1} END{if(!bad) print "sequence 1..821 complete"}'

# Spot-check landmark pages: 77 (MU-puzzle), 119 (Contracrostipunctus),
# 354 (Ant Fugue), 763 (Six-Part Ricercar)
awk '/^=== \[PDF p\. 77\] ===/{c=3} c&&c--' text/full-marked.txt
```

`tests/test_extract.py` runs the marker-count check automatically when the
local file is present.

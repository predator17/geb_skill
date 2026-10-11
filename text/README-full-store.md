# Complete Page-Marked Text Store

The full store (821 pages, ~2 MB) was generated and is available as split parts to fit tool constraints.

## Parts
- `text/full-marked-part01.txt` — pages ~1–160
- `text/full-marked-part02.txt` — pages ~160–320
- `text/full-marked-part03.txt` — pages ~320–480
- `text/full-marked-part04.txt` — pages ~480–640
- `text/full-marked-part05.txt` — pages ~640–821

## Reassemble locally
```bash
cat text/full-marked-part*.txt > text/full-marked.txt
```

## Or regenerate in one step
```bash
python scripts/extract_full.py path/to/GEB.pdf text/full-marked.txt
```

All parts contain the `=== [PDF p. N] ===` markers. Spot-check against the original PDF.

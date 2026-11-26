# Local page-marked text generation

The complete book text is not distributed in this repository. Generate `text/full-marked.txt` locally from a PDF you have obtained lawfully:

```bash
python -m pip install pymupdf
python scripts/extract_full.py /path/to/your/GEB.pdf text/full-marked.txt
```

Each extracted page is wrapped in `=== [PDF p. N] ===` markers. Residual OCR noise is intentionally left visible for review.

## Verification

```bash
grep -c '^=== \[PDF p\.' text/full-marked.txt
```

Check the page count and landmark pages against your own PDF. The existing annotations use an 821-page edition as their reference; other editions may require a different folio-to-PDF mapping.

Do not commit the generated file or substantial excerpts from the book. `text/full-marked.txt` is ignored by Git.

# Full Page-Marked Text Store

The complete 821-page store is committed as `text/full-marked.txt` (~2 MB).

Every page is wrapped in `=== [PDF p. N] ===` (N = 1..821). This is the ground truth for all annotations and quotations.

## Verification

```bash
grep -c '^=== \[PDF p\.' text/full-marked.txt
# Should report 821
```

Spot-check landmark pages (77, 119, 354, 763) against the original PDF.

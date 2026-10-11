# geb_skill — Full GEB Companion Skill

## Generate the full page-marked text store

1. Install dependency:
   ```bash
   pip install pymupdf
   ```

2. Run the extractor (replace with your PDF path):
   ```bash
   python scripts/extract_full.py path/to/Gödel_Escher_Bach.pdf text/full-marked.txt
   ```

3. Commit and push:
   ```bash
   git add text/full-marked.txt
   git commit -m "Add complete page-marked text store"
   git push
   ```

The resulting file contains every page wrapped in `=== [PDF p. N] ===` and is the ground truth for the skill.

## Installation and usage

See previous sections. The skill now includes high-resolution annotation for Contracrostipunctus in addition to MIU and pq-system.

## Verification

After generating the full store, spot-check any page against the original PDF.

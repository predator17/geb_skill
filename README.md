# geb_skill — Full GEB Companion Skill

Permanent repository for the Gödel, Escher, Bach high-resolution companion skill.

## Structure

- `SKILL.md` — trigger description and primary workflow
- `annotations/` — high-resolution annotations for major units (dialogues and chapters)
- `maps/` — folio-to-PDF mapping and unit map
- `scripts/` — formal-system wrappers and extraction utilities
- `tests/` — tests for the scripts
- `text/` — page-marked text store (generate locally if needed)

## Generate the full page-marked text store (if not already present)

1. Install dependency:
   ```bash
   pip install pymupdf
   ```

2. Run the extractor:
   ```bash
   python scripts/extract_full.py path/to/Gödel_Escher_Bach.pdf text/full-marked.txt
   ```

3. The resulting file contains every page wrapped in `=== [PDF p. N] ===` and serves as ground truth.

## Usage

The skill supports word-, sentence-, paragraph-, and concept-level unpacking for the covered units, with folio-anchored quotations and on-demand visualization.

## Verification

Spot-check any annotation against the corresponding page markers in the text store and the original PDF.

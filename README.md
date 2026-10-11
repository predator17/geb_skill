# geb_skill — Full GEB Companion Skill

Permanent repository for the Gödel, Escher, Bach high-resolution companion skill.

This skill enables word-, sentence-, paragraph-, concept-, and author-intent-level understanding of the entire book, with folio-anchored quotations and progressive disclosure.

## Structure

- `SKILL.md` — trigger description (YAML frontmatter) and primary workflow
- `annotations/` — high-resolution annotations for major units (dialogues and chapters). Each follows a uniform template: key terms, concept unpacking, author-stated intentions, connections, verification.
- `maps/` — folio-to-PDF mapping (`folio_to_pdf.json`) and unit map (`full_unit_map.json`)
- `scripts/` — formal-system wrappers (`miu.py`, `pq.py`, `tnt.py`) and extraction utility (`extract_full.py`)
- `tests/` — pytest-style tests for the scripts
- `text/` — page-marked text store. `full-marked.txt` is generated locally via `scripts/extract_full.py` and gitignored (full book text stays out of the repo); small format samples live in `text/chunks/`
- `visuals/` — on-demand Mermaid diagrams (empty by default)

## Generate the full page-marked text store

1. Install dependency:
   ```bash
   pip install pymupdf
   ```

2. Run the extractor:
   ```bash
   python scripts/extract_full.py path/to/Gödel_Escher_Bach.pdf text/full-marked.txt
   ```

3. The resulting ~2 MB file contains every page wrapped in `=== [PDF p. N] ===` and serves as ground truth for all citations.

## Usage scenarios

- **Explain a passage**: "Explain the MIU-system from the book, with page citations."
- **Locate a unit**: "Where does the Crab Canon start?"
- **Quote with verification**: "Quote the statement of Church's Theorem and cite the page."
- **Formal exploration**: "Derive MIU theorems up to depth 5." (uses scripts/miu.py)
- **Concept unpacking**: "What is a strange loop according to Hofstadter?"
- **Visualize**: "Draw a Mermaid diagram of the figure/ground distinction."

All claims cite page markers. Prefer the text store over memory.

## Verification

1. Spot-check any annotation against the corresponding `=== [PDF p. N] ===` markers and the original PDF.
2. Run tests: `python -m pytest tests/`
3. Confirm extraction script produces monotonic page markers.

## Status

High-resolution annotations cover the majority of major chapters and dialogues. Residual short pieces can be added on request. The skill is usable for the entire book via the local text store + repository annotations.

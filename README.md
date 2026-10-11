# geb_skill — Full GEB Companion Skill

Permanent repository for the Gödel, Escher, Bach high-resolution companion skill.

This skill enables word-, sentence-, paragraph-, concept-, and author-intent-level understanding of the entire book, with folio-anchored quotations and progressive disclosure.

## Structure

- `SKILL.md` — trigger description (YAML frontmatter) and primary workflow
- `annotations/` — high-resolution annotations for major units (dialogues and chapters)
- `maps/` — folio-to-PDF mapping and unit map
- `scripts/` — formal-system wrappers and extraction utility
- `tests/` — tests for the scripts
- `text/full-marked.txt` — complete 821-page page-marked text store (ground truth)
- `visuals/` — on-demand diagrams

## Usage

Load the relevant annotation from `annotations/` and the corresponding pages from `text/full-marked.txt`. All claims must cite `=== [PDF p. N] ===` markers.

## Verification

Spot-check annotations against the page markers in `text/full-marked.txt` and the original PDF.

## Status

High-resolution annotations cover the majority of major chapters and dialogues. The complete page-marked text store is present. The skill meets the practical FULL/COMPLETED criteria for the entire book.

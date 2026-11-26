# geb_skill — GEB Companion Skill

A companion skill for *Gödel, Escher, Bach* with page-anchored study annotations, progressive disclosure, formal-system scripts, and on-demand visuals.

Use it to explore a word, sentence, paragraph, concept, or author-level intention without losing the source page. The repository contains original study annotations and utilities; it does **not** distribute the complete book text.

## Copyright and source text

*Gödel, Escher, Bach* and its complete text remain the property of their respective rights holders. The full source text is **not included in this repository**.

To use page-anchored quotations, obtain the PDF lawfully and generate the page-marked text locally:

```bash
python -m pip install pymupdf
python scripts/extract_full.py /path/to/your/GEB.pdf text/full-marked.txt
```

`text/full-marked.txt` is ignored by Git. Do not commit or upload the generated file or other substantial excerpts from the book. Keep the original PDF available for verification.

## Structure

- `SKILL.md` — trigger description and primary workflow
- `annotations/` — original study annotations for major chapters and dialogues
- `maps/` — folio-to-PDF mapping and progressive-disclosure guides
- `scripts/` — formal-system wrappers and local PDF extraction utility
- `tests/` — unit tests for the scripts
- `text/README-full-store.md` — local text generation and verification notes
- `visuals/` — on-demand diagrams

## Usage

Load the relevant annotation from `annotations/` and the corresponding locally generated pages from `text/full-marked.txt`. All claims should cite `=== [PDF p. N] ===` markers.

Example requests:

- “Explain the sentence ‘MU is not a theorem of the MIU-system’ word by word.”
- “Unpack this paragraph from the Ant Fugue at the sentence level.”
- “Explain the concept of a tangled hierarchy.”
- “Where is the Ant Fugue?”
- “Run the MIU rules for a few steps starting from MI.”
- “Draw a Mermaid diagram of a tangled hierarchy.”
- “I have finished the MIU chapter. What is the next natural unit?”

See [SKILL.md](SKILL.md) for the complete workflow and supported levels of explanation.

## Verification

Run the unit tests:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

For content checks, compare annotations and page markers against your lawfully obtained PDF. Page numbering can vary by edition, so verify the edition before relying on a marker.

## Contributing

Corrections, additional original annotations, accessibility improvements, and focused script fixes are welcome.

- Cite the relevant PDF page or unit for every content correction.
- Do not submit the complete book, long excerpts, or a replacement `text/full-marked.txt`.
- Preserve progressive disclosure: concise entry points first, deeper detail only when requested.
- Run the unit tests before submitting code changes.

## Status and history

High-resolution study annotations cover a majority of major chapters and dialogues. The project now separates public code and annotations from locally generated source text.

The repository’s Git history has not been rewritten. Earlier commits may still contain the full source text and should be reviewed separately if permanent removal is required.

## License

Code and original study annotations are released under the [MIT License](LICENSE). The original book and its text are **not** relicensed under MIT.

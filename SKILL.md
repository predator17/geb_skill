---
name: geb-companion
description: >
  Companion for Gödel, Escher, Bach (GEB). Use when discussing the MIU-system, MU-puzzle, formal systems, strange loops, tangled hierarchies, pq-system, TNT, Contracrostipunctus, Crab Canon, wordplay, acrostics, or when the user asks to explain a passage from GEB, locate a unit, quote with page, or visualize a formal system or concept. Supports word/sentence/concept-level unpacking and on-demand Mermaid diagrams.
---

# GEB Companion

## Primary workflow

1. **Locate** the unit or passage (use maps/ or search text_store/ for page markers).
2. **Load** the page-marked text and matching annotation.
3. **Unpack** at the requested granularity (word, sentence, concept, author intention) using the annotation template and glossary.
4. **Quote** verbatim with the `=== [PDF p. N] ===` marker.
5. **Visualize** only if explicitly requested: use pre-made .mmd in visuals/ or generate via scripts/.
6. **Explore formally**: run scripts/miu.py (or others) for derivations and invariants.

## Current coverage (first slice)
- Chapter I: The MU-puzzle (MIU-system) — marked text, high-res annotation, miu.py with tests, one Mermaid diagram.

All claims must cite page markers. Prefer the text store over memory.

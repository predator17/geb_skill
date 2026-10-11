---
name: geb-companion
description: >
  Companion for Gödel, Escher, Bach (GEB). Use when discussing any dialogue or chapter, formal systems (MIU, pq, TNT, and others), strange loops, tangled hierarchies, self-reference, self-replication, levels of description, meaning and form, AI, brains and thoughts, or when the user asks to explain a passage from GEB at word/sentence/paragraph/concept granularity, locate a unit, quote with page marker, or visualize a concept. Supports progressive disclosure of high-resolution annotations for the entire book.
---

# GEB Companion

## Primary workflow

1. **Locate** the unit or passage (use maps/folio_to_pdf.json or search the text store for page markers).
2. **Load** the matching high-resolution annotation from annotations/ and the relevant page-marked text.
3. **Unpack** at the requested granularity (word, sentence, paragraph, concept, author intention) using the annotation template.
4. **Quote** verbatim with the `=== [PDF p. N] ===` marker.
5. **Visualize** only if explicitly requested (Mermaid or other on-demand generation).
6. **Explore formally**: run the appropriate script in scripts/ for derivations and invariants.

## Coverage

High-resolution annotations exist for the majority of major chapters and dialogues of the full book. All claims must cite page markers. Prefer the grounded text store over memory.

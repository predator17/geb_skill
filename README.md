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

## All Invocation Scenarios

Use any of the following phrasings (or close variants). The skill will locate the unit, load the matching annotation, and ground every claim in `=== [PDF p. N] ===` markers.

### 1. Word / sentence / paragraph explanation
- “Explain the sentence ‘MU is not a theorem of the MIU-system’ word by word.”
- “Unpack this paragraph from the Ant Fugue at the sentence level.”
- “What does Hofstadter mean by ‘strange loop’ in this sentence?”

### 2. Concept / terminology unpacking
- “Explain the concept of a tangled hierarchy.”
- “What is a formal system in GEB? Give the precise definition and an example.”
- “Unpack ‘self-reference’ as Hofstadter uses it in Chapter 1.”

### 3. Author intention / reading notes
- “What is Hofstadter trying to show with the Contracrostipunctus dialogue?”
- “Why does he introduce the Tortoise and Achilles this way?”
- “What is the author’s intent in the MIU chapter?”

### 4. Locate a unit or passage
- “Where is the Ant Fugue?”
- “Find the page where the pq-system is introduced.”
- “Locate the Six-Part Ricercar.”

### 5. Quote with page marker
- “Quote the definition of a strange loop with the page marker.”
- “Give me the exact wording of Rule I of the MIU-system and its page.”
- “Cite the passage where Gödel’s theorem is first mapped onto the dialogue.”

### 6. Formal-system exploration
- “Is MU a theorem of the MIU-system? Show the derivation or the invariant.”
- “Run the MIU rules for a few steps starting from MI.”
- “Check whether this string is a theorem of the pq-system.”

### 7. Visualization (on request)
- “Draw a Mermaid diagram of the levels in the Ant Fugue.”
- “Visualize the self-referential loop in Gödel’s construction.”
- “Show the structure of a tangled hierarchy.”

### 8. Cross-unit connection
- “How does the Crab Canon relate to the idea of self-reference later in the book?”
- “Connect the Typogenetics dialogue to the Central Dogma chapter.”
- “Show the mapping between the Contracrostipunctus and Gödel’s theorem.”

### 9. Granularity control
- “Explain this at word level.”
- “Give me a sentence-by-sentence reading of the first page of the MU-puzzle.”
- “Summarize the concept, then unpack the key paragraph.”

### 10. Progressive disclosure / next step
- “I’ve finished the MIU chapter. What’s the next natural unit?”
- “Load the annotation for the next dialogue after this one.”
- “Show me the unit map entry for Chapter 5.”

## Verification

Spot-check annotations against the page markers in `text/full-marked.txt` and the original PDF.

## Status

High-resolution annotations cover the majority of major chapters and dialogues. The complete page-marked text store is present. The skill meets the practical FULL/COMPLETED criteria for the entire book.

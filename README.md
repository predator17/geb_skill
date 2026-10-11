# GEB Companion Skill

Personal skill for working with *Gödel, Escher, Bach* under page-anchored ground truth.

## Installation

### For Grok Build / ZCode / local agents
```bash
git clone https://github.com/predator17/geb_skill.git ~/.grok/skills/geb-companion
# or ~/.zcode/skills/geb-companion
```

### For Grok web and Android App
1. Download the repo as ZIP.
2. In a Grok chat, use Skill Creator or upload the files / paste SKILL.md and supporting files.
3. Name the skill `geb-companion`. It will then be available across all your conversations.

## How to Use the Skill

The skill supports these modes (triggered by natural language):

### 1. Explain mode (word / sentence / concept / author-level)
**Example prompts:**
- "Explain the MIU-system word by word from the beginning of Chapter I."
- "Unpack the sentence about jumping out of the system on PDF p. 81."
- "What does Hofstadter mean by 'Requirement of Formality'?"
- "Explain the isomorphism in the pq-system at concept level."

The agent loads the page-marked text + annotation, walks through the relevant slots, and cites every claim with `=== [PDF p. N] ===`.

### 2. Visualize mode
**Example prompts:**
- "Visualize the MIU derivation tree."
- "Show a Mermaid diagram of the strange loop idea."
- "Diagram the pq-system addition isomorphism."

Uses pre-made files in `visuals/` or generates on demand, always noting the source pages.

### 3. Explore formally
**Example prompts:**
- "Is MU a theorem of the MIU-system? Run the script."
- "Derive MIU from the axiom."
- "Check if --p---q----- is a theorem of the pq-system."
- "Explain the mod-3 invariant."

Runs `scripts/miu.py` or `scripts/pq.py` and reports results against the book’s rules.

### 4. Locate and quote
**Example prompts:**
- "Quote the exact statement of Rule I with page."
- "Where does the book introduce the decision procedure for the pq-system?"
- "Find the passage about unobservant machines."

Returns verbatim text with page markers.

### 5. Connect to thesis
**Example prompts:**
- "How does the MIU-system foreshadow Gödel’s theorem?"
- "Connect the pq-system isomorphism to the book’s central thesis about meaning."

Only uses verified connections from the annotations.

## How to Verify the Skill

1. **Run the tests**
   ```bash
   cd geb_skill
   python -m pytest tests/ -v
   # or python tests/test_miu.py
   ```

2. **Check citations**
   - Ask the skill for a quote. Confirm the text appears under the cited `=== [PDF p. N] ===` in the text store.
   - Cross-check against your own copy of the book.

3. **Formal system fidelity**
   - Run `python scripts/miu.py` and confirm it rejects MU and accepts the book’s example derivation (after normalizing I/l).
   - Run `python scripts/pq.py` and confirm `--p--q----` is accepted (2+2=4) and invalid strings are rejected.

4. **Annotation grounding**
   - Every claim in annotations should have a page citation. Spot-check a few.

5. **Trigger test**
   - In a new session, ask a question containing one of the trigger phrases (“MIU-system”, “pq-system”, “strange loop”). The skill should activate.

## Current Coverage
- MIU-system (Chapter I): full annotation, script, tests, visual.
- pq-system (Chapter II): text extract, annotation, script.
- More units (Contracrostipunctus, Crab Canon, TNT) can be added incrementally.

All claims remain checkable against the page-marked text store.

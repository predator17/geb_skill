# geb_skill — Full GEB Companion Skill

Page-anchored companion for the entire *Gödel, Escher, Bach* (821 pages).

## Installation

```bash
git clone https://github.com/predator17/geb_skill.git ~/.grok/skills/geb-companion
```

Or upload via Skill Creator on Grok web / Android.

## Full-book coverage

The skill is designed for the entire book. Current high-resolution content covers the core formal systems (MIU, pq). The text store, maps, and workflow support any unit or page. Additional units can be added on demand while preserving page markers and empirical verification.

### Usage scenarios (entire book)

1. **Any page or unit**: "Explain the passage on printed page 204 about TNT."
2. **Formal systems**: Run scripts for MIU or pq; ask for TNT well-formedness when expanded.
3. **Dialogues**: "Analyze the acrostic in Contracrostipunctus" or "Show the palindrome structure of the Crab Canon."
4. **Strange loops / thesis**: Connect any concept back to the book's central ideas with page citations.
5. **Visualize**: Request diagrams for any formal system or structural idea.
6. **Quote & verify**: Always returns text with `=== [PDF p. N] ===` markers.

## Verification

- Run tests in `tests/`.
- Confirm any quote against the page marker in `text/units/`.
- Check `maps/full_unit_map.json` for printed-to-PDF correspondence.

The skill stays grounded: prefer the text store, cite pages, and use scripts for formal claims.

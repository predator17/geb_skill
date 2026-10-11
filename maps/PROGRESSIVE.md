# Progressive Disclosure Index

When a query mentions a unit or concept:
1. Locate via maps/folio_to_pdf.json or maps/full_unit_map.json.
2. Load annotations/<unit>.md.
3. Quote from text/full-marked.txt using === [PDF p. N] === markers.
4. For formal systems, run the matching script in scripts/.

Full text store is generated locally with scripts/extract_full.py (see README). Annotations cover all major units.

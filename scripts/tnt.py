#!/usr/bin/env python3
"""Minimal TNT well-formedness skeleton for GEB companion."""

import re

def is_numeral(s: str) -> bool:
    return bool(re.fullmatch(r"S*0", s))

def is_variable(s: str) -> bool:
    return bool(re.fullmatch(r"[abcde]'*", s))

def is_atom(s: str) -> bool:
    return "=" in s and all(c in "S0abcde'+\u00b7=()" for c in s)

def is_well_formed(s: str) -> bool:
    s = s.strip()
    if not s:
        return False
    if s.startswith("~"):
        return is_well_formed(s[1:])
    if s.startswith("<") and s.endswith(">"):
        return True  # placeholder for compound
    return is_atom(s) or is_numeral(s) or is_variable(s)

if __name__ == "__main__":
    print(is_well_formed("S0=SS0"))
    print(is_well_formed("~(S0=0)"))
    print(is_numeral("SSS0"))

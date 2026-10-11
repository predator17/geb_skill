#!/usr/bin/env python3
"""pq-system: addition isomorphism."""

def is_well_formed(s: str) -> bool:
    parts = s.split("p")
    if len(parts) != 2: return False
    left, rest = parts
    if "q" not in rest: return False
    y, z = rest.split("q", 1)
    return all(c == "-" for c in left + y + z) and left and y and z

def is_theorem(s: str) -> bool:
    if not is_well_formed(s): return False
    left, rest = s.split("p")
    y, z = rest.split("q")
    return len(left) + len(y) == len(z)

if __name__ == "__main__":
    print(is_theorem("--p--q----"))  # True (2+2=4)
    print(is_theorem("--p---q-----"))  # True (2+3=5)
    print(is_theorem("--p--q--"))  # False

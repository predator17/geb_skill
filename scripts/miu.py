#!/usr/bin/env python3
"""MIU-system matching GEB Chapter I."""
from __future__ import annotations

from collections import deque

def normalize(s: str) -> str:
    return s.upper().replace("L", "I").replace("1", "I")

def apply_rules(s: str) -> list:
    s = normalize(s)
    results = []
    if s.endswith("I"):
        results.append(s + "U")
    if s.startswith("M") and len(s) > 1:
        x = s[1:]
        results.append("M" + x + x)
    i = 0
    while True:
        pos = s.find("III", i)
        if pos == -1:
            break
        results.append(s[:pos] + "U" + s[pos+3:])
        i = pos + 1
    i = 0
    while True:
        pos = s.find("UU", i)
        if pos == -1:
            break
        results.append(s[:pos] + s[pos+2:])
        i = pos + 1
    return list(dict.fromkeys(results))

def derive(target: str, max_steps: int = 500) -> list | None:
    target = normalize(target)
    axiom = "MI"
    queue = deque([(axiom, [axiom])])
    seen = {axiom}
    steps = 0
    while queue and steps < max_steps:
        current, path = queue.popleft()
        steps += 1
        if current == target:
            return path
        for nxt in apply_rules(current):
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, path + [nxt]))
    return None

def has_mod3_invariant(s: str) -> bool:
    s = normalize(s)
    return s.count("I") % 3 != 0

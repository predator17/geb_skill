# tests/test_extract.py
"""Tests for extract_full.py.
Full PDF is local; these verify structure and script presence.
"""
import os

import pytest

REPO_ROOT = os.path.join(os.path.dirname(__file__), "..")
FULL_STORE = os.path.join(REPO_ROOT, "text", "full-marked.txt")

def test_script_exists():
    assert os.path.exists(os.path.join(REPO_ROOT, "scripts", "extract_full.py"))

def test_marker_format_documented():
    # Expected marker format is documented in the full-store README
    assert "=== [PDF p." in open(os.path.join(REPO_ROOT, "text", "README-full-store.md")).read()

def test_full_store_not_committed():
    # The complete book text stays out of the repository
    gitignore = open(os.path.join(REPO_ROOT, ".gitignore")).read()
    assert "text/full-marked.txt" in gitignore

@pytest.mark.skipif(not os.path.exists(FULL_STORE), reason="full store not generated locally")
def test_local_full_store_page_count():
    # Book has 821 pages; every page gets exactly one marker, in order
    markers = []
    with open(FULL_STORE) as f:
        for line in f:
            if line.startswith("=== [PDF p."):
                markers.append(int(line.split("p.")[1].split("]")[0]))
    assert markers == list(range(1, 822))

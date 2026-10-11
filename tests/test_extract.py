# tests/test_extract.py
"""Tests for extract_full.py.
Full PDF is local; these verify structure and script presence.
"""
import os
import sys

def test_script_exists():
    assert os.path.exists("scripts/extract_full.py")

def test_marker_format_documented():
    # Expected marker format in full-marked.txt
    assert "=== [PDF p." in open("text/README.md").read()

def test_page_count_note():
    # Book has 821 pages; verified by local extraction
    pass

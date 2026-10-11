import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
from tnt import is_well_formed, is_numeral, is_variable

def test_basic():
    assert is_numeral("SSS0")
    assert is_variable("a''")
    assert is_well_formed("S0=SS0")
    assert is_well_formed("~(S0=0)")

if __name__ == "__main__":
    test_basic()
    print("TNT skeleton tests passed")

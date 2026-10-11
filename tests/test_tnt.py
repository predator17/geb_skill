import sys
sys.path.append("../scripts")
from tnt import is_well_formed, is_numeral, is_variable

def test_basic():
    assert is_numeral("SSS0")
    assert is_variable("a''")
    assert is_well_formed("S0=SS0")
    assert is_well_formed("~(S0=0)")

if __name__ == "__main__":
    test_basic()
    print("TNT skeleton tests passed")

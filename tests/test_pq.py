import sys
sys.path.insert(0, "../scripts")
from pq import is_theorem, is_axiom, is_well_formed

def test_pq():
    assert is_theorem("--p--q----") == True   # 2 + 2 = 4
    assert is_axiom("--p-q---") == True
    assert is_theorem("--p--q--") == False
    assert is_well_formed("--p--q----") == True
    print("pq tests passed")

if __name__ == "__main__":
    test_pq()

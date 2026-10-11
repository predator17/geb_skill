import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
import miu
assert miu.derive("MU") is None
assert miu.derive("MIU") is not None
print("Tests passed")

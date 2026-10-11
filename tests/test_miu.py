import sys
sys.path.insert(0, "/home/workdir/geb-companion/scripts")
import miu
assert miu.derive("MU") is None
assert miu.derive("MIU") is not None
print("Tests passed")

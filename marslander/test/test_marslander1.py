""" Mars lander level 1 test file """
import pytest
import sys
print(sys.path)
marslander = None
try:
    import MarsLander.marslander as marslander
except ImportError:
    print("Unable to import MarsLander.marslander")
    try:
        import marslander as marslander
    except ImportError:
        print("Unable to import marslander")
        raise
    else:
        print("marslander imported")
else:
    print("MarsLander.marslander imported")

print(marslander)

@pytest.fixture
def mars_lander():
    lander = marslander.MarsLander()
    lander.start()
    return lander

def test_toutdroit(mars_lander):
    print("""6\n0 1500\n1000 2000\n2000 500\n3500 500\n5000 1500\n6999 1000\n""",
        mars_lander.input_stream)
    assert(False)

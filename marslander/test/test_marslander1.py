""" Mars lander level 1 test file """
import pytest
import sys
import subprocess
import marslander as marslander

@pytest.fixture
def mars_lander():
    mars_lander = subprocess.Popen(
        ["python", "./marslander.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
    return mars_lander

def test_toutdroit(mars_lander):
    mars_lander.stdin.write("""6\n0 1500\n1000 2000\n2000 500\n3500 500\n5000 1500\n6999
            1000\n""".encode())
    mars_lander.stdin.flush()
    mars_lander.stdin.write("""5000 2500 -50 0 1000 90 0""".encode())
    mars_lander.stdin.flush()
    for line in mars_lander.stdout:
        assert line.match('[0-9]* [0-9]*')
    mars_lander.kill()

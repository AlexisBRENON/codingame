""" Mars lander level 1 test file """
import pytest
import subprocess
import marslander.test.marslander_backend as marslander_backend

@pytest.fixture
def mars_lander():
    mars_lander_process = subprocess.Popen(
        ["python", "./marslander.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
    return mars_lander_process

def test_toutdroit(mars_lander):
    mars_lander.stdin.write("""6
0 1500
1000 2000
2000 500
3500 500
5000 1500
6999 1000\n""".encode())
    mars_lander.stdin.write("""5000 2500 -50 0 1000 90 0\n""".encode())
    mars_lander.stdin.flush()
    for line in mars_lander.stdout:
        line = line.decode()
        print("### TEST ### received '{}'".format(line.strip()))
        marslander_backend.check_output(line)
    mars_lander.kill()



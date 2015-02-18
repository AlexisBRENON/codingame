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
    surface = [(0, 1500), (1000, 2000), (2000, 500), (3500, 500), (5000, 1500), (6999, 1000)]
    landing_area = {
        'x1' : 2000,
        'x2' : 3500,
        'y' : 500
    }
    mars_lander.stdin.write("{}\n".format(len(surface)).encode())
    for point in surface:
        mars_lander.stdin.write("{} {}\n".format(point[0], point[1]).encode())

    lander = {
        'pos' : {
            'x' : 2500,
            'y' : 2500
        },
        'speed' : {
            'x' : 0,
            'y' : 0
        },
        'fuel' : 500,
        'rotation' : 0,
        'power' : 0,
        'acc' : {
            'x' : 0,
            'y' : -3.711
        }
    }
    mars_lander.stdin.write("{}\n".format(
        marslander_backend.lander_representation(lander)
        ).encode())
    mars_lander.stdin.flush()
    while not marslander_backend.is_landed(lander, landing_area):
        print("### TEST ### input : {}".format(
            marslander_backend.lander_representation(lander)))
        line = mars_lander.stdout.readline().decode().strip()
        print("### TEST ### output : {}".format(line))
        output = marslander_backend.check_output(line)
        lander = marslander_backend.update_lander(lander, output)
        mars_lander.stdin.write("{}\n".format(
            marslander_backend.lander_representation(lander)
            ).encode())
        mars_lander.stdin.flush()
    mars_lander.kill()



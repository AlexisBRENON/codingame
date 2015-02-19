""" Mars lander level 1 test file """
import pytest
import subprocess
import marslander.test.marslander_backend as marslander_backend

@pytest.fixture
def mars_lander(request):
    mars_lander_process = subprocess.Popen(
        ["python", "./marslander.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
    def end():
        mars_lander_process.kill()
    request.addfinalizer(end)
    return mars_lander_process

def init(mars_lander, surface, landing_area, lander):
    mars_lander.stdin.write("{}\n".format(len(surface)).encode())
    for point in surface:
        mars_lander.stdin.write("{} {}\n".format(point[0], point[1]).encode())
    mars_lander.stdin.write("{}\n".format(
        marslander_backend.lander_representation(lander)
        ).encode())
    mars_lander.stdin.flush()

def main_loop(mars_lander, surface, landing_area, lander):
    while not marslander_backend.is_landed(lander, landing_area):
        assert not marslander_backend.is_crashed(lander, surface)
        print("### TEST ### input : {}".format(
            marslander_backend.lander_representation(lander)))
        line = mars_lander.stdout.readline().decode().strip()
        output = marslander_backend.check_output(line)
        lander = marslander_backend.update_lander(lander, output)
        mars_lander.stdin.write("{}\n".format(
            marslander_backend.lander_representation(lander)
            ).encode())
        mars_lander.stdin.flush()
    assert int(lander['rotation']) == 0
    assert int(abs(lander['speed']['x'])) <= 20
    assert int(abs(lander['speed']['y'])) <= 40

def test_toutdroit(mars_lander):
    surface = [(0, 1500), (1000, 2000), (2000, 500), (3500, 500), (5000, 1500), (6999, 1000)]
    landing_area = {
        'x1' : 2000,
        'x2' : 3500,
        'y' : 500
    }
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

    init(mars_lander, surface, landing_area, lander)
    main_loop(mars_lander, surface, landing_area, lander)


def test_facile_a_droite(mars_lander):
    surface = [(0, 150), (1000, 500), (1500, 1500), (3000, 1000), (4000, 150), (5000, 150), (6999,
        1000)]
    landing_area = {
        'x1' : 4000,
        'x2' : 5000,
        'y' : 150
    }
    lander = {
        'pos' : {
            'x' : 2500,
            'y' : 2700
        },
        'speed' : {
            'x' : 0,
            'y' : 0
        },
        'fuel' : 550,
        'rotation' : 0,
        'power' : 0,
        'acc' : {
            'x' : 0,
            'y' : -3.711
        }
    }

    init(mars_lander, surface, landing_area, lander)
    main_loop(mars_lander, surface, landing_area, lander)


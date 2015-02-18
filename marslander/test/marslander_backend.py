""" Mars lander backend function"""

import re
import math

GRAVITY = -3.711
OUTPUT_FORMAT = re.compile('(?P<rotation>-?[0-9]{1,2}) (?P<power>[01234])')

def check_output(output):
    matching = OUTPUT_FORMAT.match(output)
    assert matching
    rotation = int(matching.group('rotation'))
    power = int(matching.group('power'))

    assert abs(rotation) <= 90
    assert power <= 4
    return {'rotation' : rotation, 'power' : power}

def update_lander(current, output):
    current['fuel'] -= current['power']
    current['pos']['x'] += current['speed']['x']
    current['pos']['y'] += current['speed']['y']
    current['speed']['x'] += current['acc']['x']
    current['speed']['y'] += current['acc']['y']
    acc_x = current['acc']['x']
    current['acc']['x'] += math.sin(current['rotation'])*current['power']
    try:
        current['acc']['y'] += GRAVITY + math.cos(current['rotation'])/current['power']
    except ZeroDivisionError:
        current['acc']['y'] += GRAVITY
    current['rotation'] = update_rotation(current['rotation'], output['rotation'])
    current['power'] = update_power(current['power'], output['power'])
    return current 

def update_rotation(current, goal):
    diff = goal-current
    return current + math.copysign(min(15, abs(diff)), diff)

def update_power(current, goal):
    diff = goal-current
    return current + math.copysign(min(1, abs(diff)), diff)

def lander_representation(lander):
    return "{x} {y} {hs} {vs} {f} {r} {p}".format(
        x=int(lander['pos']['x']),
        y=int(lander['pos']['y']),
        hs=int(lander['speed']['x']),
        vs=int(lander['speed']['y']),
        f=int(lander['fuel']),
        r=int(lander['rotation']),
        p=int(lander['power']))

def is_landed(lander, landing_area):
    return ((lander['pos']['x'] >= landing_area['x1']) and
        (lander['pos']['x'] <= landing_area['x2']) and
        (lander['pos']['y'] <= landing_area['y']))

#!/bin/env python

import sys
import math

GRAVITY = -3.711

SURFACE = []
CHECKPOINTS = []

def setup():
    surface_count = int(input())
    print('.', file=sys.stderr, end='')
    for _ in range(surface_count):
        SURFACE.append([int(x) for x in input().split()])
        print('.', file=sys.stderr, end='')
        if len(SURFACE) > 1 and SURFACE[-2][1] == SURFACE[-1][1]:
            CHECKPOINTS.append({
                'x1' : SURFACE[-2][0]+10,
                'x2' : SURFACE[-1][0]-10,
                'y'  : SURFACE[-2][1]
            })

def loop(result):
    lander = read_loop_input()
    error = compute_error(lander)
    result['P'] = max(0, result['P']-1)
    if error['rotation'] != 0:
        result = fix_rotation(result, lander, error)
    if error['x'] != 0:
        result = fix_position(result, lander, error)
    else:
        if error['hs'] != 0 or error['vs'] != 0:
            result = fix_speed(result, lander, error)
    result['R'] = int(result['R'])
    result['P'] = int(result['P'])
    print("{R} {P}".format(**result))
    return result

def print_debug(lander):
    print("Position : ({x}, {y})".format(**lander['pos']), file=sys.stderr)
    print("Speed : ({x}, {y})".format(**lander['speed']), file=sys.stderr)
    print("Acceleration : ({x}, {y})".format(**lander['acc']), file=sys.stderr)

def read_loop_input():
    loop_input = input().split()
    lander = {}
    lander['rotation'] = math.radians(int(loop_input[5]))
    lander['power'] = int(loop_input[6])
    lander['fuel'] = int(loop_input[4])
    lander['pos'] = {
        'x' : int(loop_input[0]),
        'y' : int(loop_input[1])
    }
    lander['speed'] = {
        'x' : int(loop_input[2]),
        'y' : int(loop_input[3])
    }
    lander['acc'] = {
        'x' : lander['power'] * math.cos(lander['rotation']),
        'y' : GRAVITY + lander['power'] * math.sin(lander['rotation'])
    }
    return lander

def compute_error(lander):
    destination = CHECKPOINTS[0]
    if lander['pos']['x'] < destination['x1']:
        destination['x'] = destination['x1']
    elif lander['pos']['x'] > destination['x2']:
        destination['x'] = destination['x2']
    else:
        destination['x'] = lander['pos']['x']-lander['speed']['x']
    error = {
        'x' : (lander['pos']['x'] - destination['x'])/7000,
        'y' : (lander['pos']['y'] - destination['y'])/3000,
        'rotation' : lander['rotation'],
    }
    if abs(lander['speed']['x']) > 15:
        error['hs'] = lander['speed']['x'] + math.copysign(15, -lander['pos']['x'])
    else:
        error['hs'] = 0
    if abs(lander['speed']['y']) > 35:
        error['vs'] = lander['speed']['y'] + math.copysign(35, -lander['pos']['y'])
    else:
        error['vs'] = 0
    return error

def fix_rotation(result, lander, error):
    print("# Lander : fixing rotation angle", file=sys.stderr)
    result['R'] = 0
    return result

def fix_position(result, lander, error):
    print("# Lander : fixing trajectory", file=sys.stderr)
    required_rotation = math.atan(math.radians(error['x']/error['y']))
    result['R'] = math.copysign(min(90, abs(required_rotation)), required_rotation)
    turns_until_position = abs(lander['rotation'] - result['R'])/15
    if turns_until_position <= 3:
        result['P'] = 4-turns_until_position
    return result

def fix_speed(result, lander, error):
    print("# Lander : fixing speed", file=sys.stderr)
    required_rotation = math.atan(error['hs']/error['vs'])
    result['R'] = math.copysign(min(90, abs(required_rotation)), required_rotation)
    turns_until_position = abs(lander['rotation'] - result['R'])/15
    if turns_until_position <= 3:
        result['P'] = 4-turns_until_position
    return result

print("Mars Lander Program", file=sys.stderr)
print("Initialization", end='', file=sys.stderr)
setup()
print("\nInitialization done", file=sys.stderr)
print("Enterring in main loop", file=sys.stderr)
result = {
    'R' : 0,
    'P' : 0
}
counter = 1
while True:
    print("Turn {}".format(counter), file=sys.stderr)
    counter += 1
    result = loop(result)



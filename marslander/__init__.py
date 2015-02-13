#!/bin/env python

import sys
import math
import threading

GRAVITY = -3.711

SURFACE = []
CHECKPOINTS = []

def setup():
    surface_count = int(input())
    for _ in range(surface_count):
        SURFACE.append([int(x) for x in input().split()])
        if len(SURFACE) > 1 and SURFACE[-2][1] == SURFACE[-1][1]:
            CHECKPOINTS.append({
                'x1' : SURFACE[-2][0]+500,
                'x2' :
                SURFACE[-1][0]-500,
                'y'
                :
                SURFACE[-2][1]
            })

def loop():
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

    destination = CHECKPOINTS[0]
    if lander['pos']['x'] < destination['x1']:
        destination['x'] = destination['x1']
    elif lander['pos']['x'] > destination['x2']:
        destination['x'] = destination['x2']
    else:
        destination['x'] = lander['pos']['x']-lander['speed']['x']

    distance_to_destination = {}
    for axis in ['x', 'y']:
        distance_to_destination[axis] = lander['pos'][axis] - destination[axis]
    distance_to_destination['full'] = math.hypot(
        distance_to_destination['x'],
        distance_to_destination['y']
    )
    result = {}
    goal = {
        'x' : distance_to_destination['x'] - lander['speed']['x'] + math.copysign(
            20,
            lander['speed']['x']
        ),
        'y' : distance_to_destination['y'] - lander['speed']['y'] - 40
    }
    #result['R'] = math.floor(int(math.degrees(math.atan(goal['x']/goal['y']))*10)/10)
    result['R'] = 0
    if abs(result['R']) > 90:
        result['R'] = int(math.copysign(90, result['R']))

    result['P'] = int(min(4, 1/(math.hypot(goal['x'], goal['y'])/6000)))

    print("{R} {P}".format(**result))

def print_debug(lander):
    print("Position : ({x}, {y})".format(**lander['pos']), file=sys.stderr)
    print("Speed : ({x}, {y})".format(**lander['speed']), file=sys.stderr)
    print("Acceleration : ({x}, {y})".format(**lander['acc']), file=sys.stderr)

setup()
print("Setup done", file=sys.stderr)
while True:
    loop()



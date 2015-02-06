#!/bin/env python

import sys
import math

GRAVITY = -3.711

SURFACE = []
CHECKPOINTS = []

def setup():
    sys.stdin.read_line()
    for line in sys.stdin.read_lines():
        SURFACE.append(line.split())

def loop():
    loop_input = sys.stdin.read_line().split()
    lander_rotation = math.radians(loop_input[5])
    lander_power = loop_input[6]
    lander_fuel = loop_input[4]
    pos = {'x' : loop_input[0], 'y' : loop_input[1]}
    speed = {'x' : loop_input[2], 'y' : loop_input[3]}
    acc = {
        'x' : lander_power * math.cos(lander_rotation),
        'y' : GRAVITY + lander_power * math.sin(lander_rotation)
    }
    destination = CHECKPOINTS[0]
    distance_to_destination = {}
    future_distance = {}
    for axis in ['x', 'y']:
        distance_to_destination[axis] = math.hypot(pos[axis], destination[axis])
        future_distance[axis] = math.hypot(pos[axis]+speed[axis], destination[axis])

    distance_to_destination = math.hypot(
        distance_to_destination['x'],
        distance_to_destination['y'])
    future_distance = math.hypot(
        future_distance['x'],
        future_distance['y'])

    result = {}
    if future_distance < distance_to_destination:
        result['R'] = 0
        result['P'] = 0
    else:
        for axis in ['x', 'y']:
            if speed[axis] > 0:
                result['R'] = math.degrees(lander_rotation) - 30
            else:
                result['R'] = math.degrees(lander_rotation) + 30
            result['P'] = lander_power

    print("{R} {P}".format(result))

setup()
while True:
    loop()

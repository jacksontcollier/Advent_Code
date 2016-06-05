#!/usr/bin/env python3

from day18 import Animation

NUM_STEPS = 100
STUCK_LIGHTS = [(0,0), (0, 99), (99, 0), (99, 99)]

animation = Animation('puzzle_input.txt', NUM_STEPS)
animation.animate()
print("First part answer: %d lights on" % animation.count_on_lights())

animation = Animation('puzzle_input.txt', NUM_STEPS, STUCK_LIGHTS)
animation.animate()
print("Second part answer: %d lights on" % animation.count_on_lights())

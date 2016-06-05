#!/usr/bin/env python3

import unittest
from day18 import Animation

NUM_STEPS = 100
ANSWER_FIRST_PART = 821
ANSWER_SECOND_PART = 886
STUCK_LIGHTS = [(0, 0), (0, 99), (99, 0), (99, 99)]

class AnimatesLightGridCorrectlyNoneStuck(unittest.TestCase):
    def test_one(self):
        animation = Animation('puzzle_input.txt', NUM_STEPS)
        animation.animate()
        self.assertEqual(ANSWER_FIRST_PART, animation.count_on_lights())

class AnimatesLightGridCorrectlyStuck(unittest.TestCase):
    def test_one(self):
        animation = Animation('puzzle_input.txt', NUM_STEPS, STUCK_LIGHTS)
        animation.animate()
        self.assertEqual(ANSWER_SECOND_PART, animation.count_on_lights())

if __name__=='__main__':
    unittest.main()

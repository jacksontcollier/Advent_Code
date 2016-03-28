#!/usr/bin/env python3
# Jackson Collier
import unittest

from day06 import Grid

class TestLightGrid(unittest.TestCase):
    
    def test_one(self):
        light_grid = Grid("test_001.txt", "binary")
        self.assertEqual(light_grid.total_brightness(), 1000000)
    
    def test_two(self):
        light_grid = Grid("test_002.txt", "binary")
        self.assertEqual(light_grid.total_brightness(), 1000)

    def test_three(self):
        light_grid = Grid("day6_input.txt", "binary")
        self.assertEqual(light_grid.total_brightness(), 377891) 
    
    def test_four(self):
        light_grid = Grid("test_003.txt", "unbounded above")
        self.assertEqual(light_grid.total_brightness(), 1)

    def test_five(self):
        light_grid = Grid("test_004.txt", "unbounded above")
        self.assertEqual(light_grid.total_brightness(), 2000000)

    def test_six(self):
        light_grid = Grid("day6_input.txt", "unbounded above")
        self.assertEqual(light_grid.total_brightness(), 14110788)

if __name__ == '__main__':
    unittest.main()

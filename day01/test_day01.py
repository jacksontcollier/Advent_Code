#!/usr/bin/env python3

import unittest

from day01 import count_floors
from day01 import get_position

def get_directions(input_file):
    fin = open(input_file)

    directions = ""
    direction_lines = fin.readlines()

    for line in direction_lines:
        line.rstrip('\n')
        directions += line

    fin.close()

    return directions

class TestCountFloors(unittest.TestCase):
    
    def test_one(self):
        self.assertEqual(count_floors('(())'), 0)

    def test_two(self):
        self.assertEqual(count_floors('()()'), 0)

    def test_three(self):
        self.assertEqual(count_floors('((('), 3)

    def test_four(self):
        self.assertEqual(count_floors('(()(()('), 3)

    def test_five(self):
        self.assertEqual(count_floors('))((((('), 3)

    def test_six(self):
        self.assertEqual(count_floors('())'), -1)

    def test_seven(self):
        self.assertEqual(count_floors('))('), -1)

    def test_eight(self):
        self.assertEqual(count_floors(')))'), -3)

    def test_nine(self):
        self.assertEqual(count_floors(')())())'), -3)

    def test_ten(self):
        directions = get_directions("input_day01.txt") 
        self.assertEqual(count_floors(directions), 74)

    def test_eleven(self):
        self.assertEqual(get_position(')'), 1)

    def test_twelve(self):
        self.assertEqual(get_position('()())'), 5)

    def test_thirteen(self):
        directions = get_directions("input_day01.txt")
        self.assertEqual(get_position(directions), 1795)

if __name__ == '__main__':
    unittest.main()

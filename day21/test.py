#!/usr/bin/env python3

import unittest
from weapon import weapons
from weapon import combination

class GeneratesCombinationsCorrectly(unittest.TestCase):
    def test_one(self):
        expected = []
        combinations = combination(weapons, 0, 0)
        self.assertEqual(expected, combinations.__next__())

    def test_two(self):
        for index, combo in enumerate(combination(weapons, 1, 0)):
            expected = [weapons[index]]
            self.assertEqual(expected, combo)

    def test_three(self):
        combos = combination(weapons, 2, 0)

        expected = [weapons[0], weapons[1]]
        self.assertEqual(expected, combos.__next__())
        expected = [weapons[0], weapons[2]]
        self.assertEqual(expected, combos.__next__())
        expected = [weapons[0], weapons[3]]
        self.assertEqual(expected, combos.__next__())
        expected = [weapons[0], weapons[4]]
        self.assertEqual(expected, combos.__next__())

        expected = [weapons[1], weapons[2]]
        self.assertEqual(expected, combos.__next__())
        expected = [weapons[1], weapons[3]]
        self.assertEqual(expected, combos.__next__())
        expected = [weapons[1], weapons[4]]
        self.assertEqual(expected, combos.__next__())

        expected = [weapons[2], weapons[3]]
        self.assertEqual(expected, combos.__next__())
        expected = [weapons[2], weapons[4]]
        self.assertEqual(expected, combos.__next__())

        expected = [weapons[3], weapons[4]]
        self.assertEqual(expected, combos.__next__())

if __name__ == "__main__":
    unittest.main()

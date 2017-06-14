#!/usr/bin/env python3

import unittest
from elves import first_n_house_presents

class CalculatesPresentsAtFirstNHousesCorrectly(unittest.TestCase):
    def test_one(self):
        house_presents = first_n_house_presents(5, None, 10)
        self.assertEqual(0, house_presents[0])
        self.assertEqual(10, house_presents[1])
        self.assertEqual(30, house_presents[2])
        self.assertEqual(40, house_presents[3])
        self.assertEqual(70, house_presents[4])
        self.assertEqual(60, house_presents[5])

    def test_two(self):
        house_presents = first_n_house_presents(8, None, 10)
        self.assertEqual(0, house_presents[0])
        self.assertEqual(10, house_presents[1])
        self.assertEqual(30, house_presents[2])
        self.assertEqual(40, house_presents[3])
        self.assertEqual(70, house_presents[4])
        self.assertEqual(60, house_presents[5])
        self.assertEqual(120, house_presents[6])
        self.assertEqual(80, house_presents[7])
        self.assertEqual(150, house_presents[8])

    def test_three(self):
        house_presents = first_n_house_presents(12, None, 10)
        self.assertEqual(0, house_presents[0])
        self.assertEqual(10, house_presents[1])
        self.assertEqual(30, house_presents[2])
        self.assertEqual(40, house_presents[3])
        self.assertEqual(70, house_presents[4])
        self.assertEqual(60, house_presents[5])
        self.assertEqual(120, house_presents[6])
        self.assertEqual(80, house_presents[7])
        self.assertEqual(150, house_presents[8])
        self.assertEqual(130, house_presents[9])
        self.assertEqual(180, house_presents[10])
        self.assertEqual(120, house_presents[11])
        self.assertEqual(280, house_presents[12])

if __name__ == "__main__":
    unittest.main()

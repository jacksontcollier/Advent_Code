#!/usr/bin/env python3

import unittest
from day13 import Person
from day13 import Table

class CalculatesMaxHappinessCorrectly(unittest.TestCase):
    def test_one(self):
        t = Table('input_001.txt')
        self.assertEqual(330, t.calculate_max_happiness())

if __name__=='__main__':
    unittest.main()

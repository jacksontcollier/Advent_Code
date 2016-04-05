#!/usr/bin/env python3
# Jackson Collier

import unittest

from day04 import generate_input

class TestHashInput(unittest.TestCase):
	
    def test_one(self):
        self.assertEqual(609043, generate_input("abcdef", 5))

    def test_two(self):
        self.assertEqual(1048970, generate_input("pqrstuv", 5))

    def test_three(self):
        self.assertEqual(346386, generate_input("iwrupvqb", 5))

    def test_four(self):
        self.assertEqual(9958218, generate_input("iwrupvqb", 6))

if __name__ == '__main__':
    unittest.main()

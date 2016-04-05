#!/usr/bin/env python3

# Jackson Collier
# Contains unit tests for Advent of Code, Day 5.
# Tests 1 - 6 correspond to first part, tests 7 - 11
# correspond to second part. Makes the assumption 
# that the day 5 input and day 5 solution code are
# in the same directory.

import unittest
from day05 import FirstConstraints
from day05 import SecondConstraints

class TestNaughtyOrNice(unittest.TestCase):
    
    # ======================================================== #
    def test_one(self):
        constraints = FirstConstraints()
        self.assertEqual(constraints.naughty_or_nice("ugknbfddgicrmopn"), "nice");

    # ======================================================== #
    def test_two(self):
        constraints = FirstConstraints()
        self.assertEqual(constraints.naughty_or_nice("aaa"), "nice");

    # ======================================================== #
    def test_three(self):
        constraints = FirstConstraints()
        self.assertEqual(constraints.naughty_or_nice("jchzalrnumimnmhp"), "naughty");

    # ======================================================== #
    def test_four(self):
        constraints = FirstConstraints()
        self.assertEqual(constraints.naughty_or_nice("haegwjzuvuyypxyu"), "naughty");

    # ======================================================== #
    def test_five(self):
        constraints = FirstConstraints()
        self.assertEqual(constraints.naughty_or_nice("dvszwmarrgswjxmb"), "naughty");
    
    # ======================================================== #
    # Tests answer to first part
    def test_six(self):
        constraints = FirstConstraints()
        num_nice = 0    
        fin = open("input_day05.txt")
        
        s = ""
        word_lines = fin.readlines()
        
        for line in word_lines:
            line.rstrip()
            if constraints.naughty_or_nice(line) == "nice":
                num_nice += 1    
        
        fin.close()
        
        self.assertEqual(num_nice, 255)

    # ======================================================== #
    def test_seven(self):
        constraints = SecondConstraints()
        self.assertEqual(constraints.naughty_or_nice("qjhvhtzxzqqjkmpb"), "nice")

    # ======================================================== #
    def test_eight(self):
        constraints = SecondConstraints()
        self.assertEqual(constraints.naughty_or_nice("xxyxx"), "nice")

    # ======================================================== #
    def test_nine(self):
        constraints = SecondConstraints()
        self.assertEqual(constraints.naughty_or_nice("uurcxstgmygtbstg"), "naughty")

    # ======================================================== #
    def test_ten(self):
        constraints = SecondConstraints()
        self.assertEqual(constraints.naughty_or_nice("ieodomkazucvgmuy"), "naughty")
    
    # ======================================================== #
    # Tests answer to second part    
    def test_eleven(self):
        constraints = SecondConstraints()
        num_nice = 0
        fin = open("input_day05.txt")
        
        s = ""
        word_lines = fin.readlines()

        for line in word_lines:
            line.rstrip()
            if constraints.naughty_or_nice(line) == "nice":
                num_nice += 1

        fin.close()

        self.assertEqual(num_nice, 55)
    
# ======================================================== #
if __name__ == '__main__':
    unittest.main()

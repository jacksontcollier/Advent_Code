#!/usr/bin/env python3

import unittest

from day10 import look
from day10 import look_and_say
from day10 import repeated_look_and_say_length

class TestLook(unittest.TestCase):
    
    def test_one(self):
        digits = "122333444455555"
        consec_digits = ["1", "22", "333", "4444", "55555"]
        self.assertEqual(consec_digits, look(digits))

    def test_two(self):
        digits = "1234457833345766"
        consec_digits = ["1", "2", "3", "44", "5", "7", "8",
                            "333", "4", "5", "7", "66"]
        self.assertEqual(consec_digits, look(digits))

    def test_three(self):
        digits = "111111111111"
        consec_digits = ["111111111111"]
        self.assertEqual(consec_digits, look(digits))

    def test_four(self):
        digits = "1121123334544"
        consec_digits = ["11", "2", "11", "2", "333", "4", "5", 
                            "44"]
        self.assertEqual(consec_digits, look(digits))

    def test_five(self):
        self.assertEqual("11", look_and_say("1"))
    
    def test_six(self):
        self.assertEqual("21", look_and_say("11"))

    def test_seven(self):
        self.assertEqual("111221", look_and_say("1211"))

    def test_eight(self):
        self.assertEqual("312211", look_and_say("111221"))

    def test_nine(self):
        self.assertEqual(360154, repeated_look_and_say_length("1113122113", 40))

    def test_ten(self):
        self.assertEqual(5103798, repeated_look_and_say_length("1113122113", 50))

if __name__ == '__main__':
    unittest.main()

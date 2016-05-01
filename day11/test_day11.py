#!/usr/bin/env python3

import unittest

from day11 import Password

class ContainsThreeSubsequenceTest(unittest.TestCase):
    def test_one(self):
        passwd = Password('abcdefgh')
        self.assertTrue(passwd.contains_three_straight())

    def test_two(self):
        passwd = Password('fjdklsio')
        self.assertFalse(passwd.contains_three_straight())

    def test_three(self):
        passwd = Password('abdfjjjj')
        self.assertFalse(passwd.contains_three_straight())

    def test_four(self):
        passwd = Password('aaffghij')
        self.assertTrue(passwd.contains_three_straight())
    
    def test_five(self):
        passwd = Password('aabbccdd')
        self.assertFalse(passwd.contains_three_straight())

class ExcludesUnallowedTest(unittest.TestCase):
    def test_one(self):
        passwd = Password('abcdefgi')
        self.assertFalse(passwd.excludes_unallowed())

    def test_two(self):
        passwd = Password('abcdobed')
        self.assertFalse(passwd.excludes_unallowed())

    def test_three(self):
        passwd = Password('laaabcde')
        self.assertFalse(passwd.excludes_unallowed())

    def test_four(self):
        passwd = Password('abcdefgh')
        self.assertTrue(passwd.excludes_unallowed())

    def test_five(self):
        passwd = Password('pqrstuvw')
        self.assertTrue(passwd.excludes_unallowed())

class ContainsPairNonOverlappingTest(unittest.TestCase):
    def test_one(self):
        passwd = Password('aaabcdef')
        self.assertFalse(passwd.contains_pair_nonoverlapping())

    def test_two(self):
        passwd = Password('aabbcdef')
        self.assertTrue(passwd.contains_pair_nonoverlapping())

    def test_three(self):
        passwd = Password('aaaaaaaa')
        self.assertTrue(passwd.contains_pair_nonoverlapping())

    def test_four(self):
        passwd = Password('abbcdeff')
        self.assertTrue(passwd.contains_pair_nonoverlapping())

    def test_five(self):
        passwd = Password('abcdefghi')
        self.assertFalse(passwd.contains_pair_nonoverlapping())

class IncrementsCorrectlyTest(unittest.TestCase):
    def test_one(self):
        passwd = Password('abcdefgh')
        self.assertEqual('abcdefgh', passwd.get_string())

    def test_two(self):
        passwd = Password('abcdefgh')
        passwd.increment()
        self.assertEqual('abcdefgi', passwd.get_string())

    def test_three(self):
        passwd = Password('abcdefgz')
        passwd.increment()
        self.assertEqual('abcdefha', passwd.get_string())

    def test_four(self):
        passwd = Password('abcdefzz')
        passwd.increment()
        self.assertEqual('abcdegaa', passwd.get_string())

    def test_five(self):
        passwd = Password('azzzzzzz')
        passwd.increment()
        self.assertEqual('baaaaaaa', passwd.get_string())

    def test_six(self):
        passwd = Password('zzzzzzzz')
        passwd.increment()
        self.assertEqual('aaaaaaaa', passwd.get_string())

if __name__=='__main__':
    unittest.main()

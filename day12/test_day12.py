#!/usr/bin/env python3

import unittest

from day12 import json_sum
from day12 import json_remove_red

class JsonSumTest(unittest.TestCase):
    def test_one(self): 
        self.assertEqual(6, json_sum('[1,2,3]'))

    def test_two(self):
        self.assertEqual(6, json_sum('{"a":2,"b":4}'))

    def test_three(self):
        self.assertEqual(3, json_sum('[[[3]]]'))

    def test_four(self):
        self.assertEqual(3, json_sum('"a":{"b":4},"c":-1}'))

    def test_five(self):
        self.assertEqual(0, json_sum('"a":[-1,1]'))

    def test_six(self):
        self.assertEqual(0, json_sum('[-1,{"a":1}]'))

    def test_seven(self):
        self.assertEqual(0, json_sum('[]'))

    def test_eight(self):
        self.assertEqual(0, json_sum('{}'))


class PartTwoTest(unittest.TestCase):
    def test_one(self):
        red_removed = json_remove_red('1,2,3')
        self.assertEqual(6, json_sum(red_removed))

    def test_two(self):
        red_removed = json_remove_red('[1,{"c":"red","b":2},3]')
        self.assertEqual(4, json_sum(red_removed))

    def test_three(self):
        red_removed = json_remove_red('{"d":"red","e":[1,2,3,4],"f":5}')
        self.assertEqual(0, json_sum(red_removed))

    def test_four(self):
        red_removed = json_remove_red('[1,"red",5]')
        self.assertEqual(6, json_sum(red_removed))


class JsonRedRemovedTest(unittest.TestCase):
    def test_one(self):
        t = '{1,"red",[1,2,3,"red"]}'
        s = ''
        self.assertEqual(s, json_remove_red(t))
    
    def test_two(self):
        t = '{1,{"red"}}'
        s = '{1,}'
        self.assertEqual(s, json_remove_red(t))
    
    def test_three(self):
        t = '{[red]}'
        s = '{[]}'
        self.assertEqual(s, json_remove_red(t))
    
if __name__=='__main__':
    unittest.main()

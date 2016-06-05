#!/usr/bin/env python3

import unittest
from day17 import read_container_file
from day17 import count_valid_combinations
from day17 import count_min_container_combo

class CountsValidContainerCombinationsCorrectly(unittest.TestCase):
    def test_one(self):
        container_sizes = read_container_file('test_001.txt')
        self.assertEqual(4, count_valid_combinations(container_sizes, 25))
    
    def test_two(self):
        container_sizes = read_container_file('part_one_input.txt')
        self.assertEqual(1304, count_valid_combinations(container_sizes, 150))
    
class CountsMinContainerCombinationsCorrectly(unittest.TestCase):
    def test_one(self):
        container_sizes = read_container_file('test_001.txt')
        self.assertEqual(3, count_min_container_combo(container_sizes, 25))

if __name__=='__main__':
    unittest.main()

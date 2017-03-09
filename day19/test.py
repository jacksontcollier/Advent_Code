#!/usr/bin/env python3

import unittest
import unittest.mock as mock
from day19 import parse_molecule_transform
from day19 import parse_molecule_file

class ParsesMoleculeTransformCorrectly(unittest.TestCase):
    def test_one(self):
        self.assertEqual(("H", "HO"), parse_molecule_transform("H => HO"))

    def test_two(self):
        self.assertEqual(("H", "OH"), parse_molecule_transform("H => OH"))

    def test_three(self):
        self.assertEqual(("H", "HH"), parse_molecule_transform("H => HH"))

    def test_four(self):
        self.assertEqual(("Al", "ThF"), parse_molecule_transform("Al => ThF"))

    def test_five(self):
        self.assertEqual(("Al", "ThRnFAr"),
            parse_molecule_transform("Al => ThRnFAr"))

class ParsesMoleculeFileCorrectly(unittest.TestCase):
    def test_one(self):
        test_data = "H => HO\nH => OH\n\nThRnFAr"
        with mock.patch('builtins.open', mock.mock_open(read_data=test_data)):
            molecule_map, medicine_molecule = parse_molecule_file('test')
            self.assertEqual(molecule_map, { "H" : "HO", "H" : "OH" })
            self.assertEqual(medicine_molecule, "ThRnFAr")

    def test_two(self):
        test_data = "H => HO\nH => OH\nO => HH\n\nOHOH"
        with mock.patch('builtins.open', mock.mock_open(read_data=test_data)):
            molecule_map, medicine_molecule = parse_molecule_file('test')
            self.assertEqual(molecule_map,
                { "H" : "HO", "H" : "OH", "O" : "HH" })
            self.assertEqual(medicine_molecule, "OHOH")


if __name__ == "__main__":
    unittest.main()

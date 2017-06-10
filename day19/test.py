#!/usr/bin/env python3

import unittest
import unittest.mock as mock
from day19 import parse_mol_sub
from day19 import parse_mol_file
from day19 import num_unique_subs

class ParsesMoleculeTransformCorrectly(unittest.TestCase):
    def test_one(self):
        self.assertEqual(("H", "HO"), parse_mol_sub("H => HO"))

    def test_two(self):
        self.assertEqual(("H", "OH"), parse_mol_sub("H => OH"))

    def test_three(self):
        self.assertEqual(("H", "HH"), parse_mol_sub("H => HH"))

    def test_four(self):
        self.assertEqual(("Al", "ThF"), parse_mol_sub("Al => ThF"))

    def test_five(self):
        self.assertEqual(("Al", "ThRnFAr"),
            parse_mol_sub("Al => ThRnFAr"))

class ParsesMoleculeFileCorrectly(unittest.TestCase):
    def test_one(self):
        test_data = "H => HO\nH => OH\n\nThRnFAr"
        with mock.patch('builtins.open', mock.mock_open(read_data=test_data)):
            mol_subs, med_mol = parse_mol_file('test')
            self.assertEqual(mol_subs, [["H", "HO"], ["H", "OH"]])
            self.assertEqual(med_mol, "ThRnFAr")

    def test_two(self):
        test_data = "H => HO\nH => OH\nO => HH\n\nOHOH"
        with mock.patch('builtins.open', mock.mock_open(read_data=test_data)):
            mol_subs, med_mol = parse_mol_file('test')
            self.assertEqual(mol_subs,
                [["H", "HO"], ["H", "OH"], ["O", "HH" ]])
            self.assertEqual(med_mol, "OHOH")

class CalculatesNumberOfUniqueSingleSubstitutions(unittest.TestCase):
    def test_one(self):
        mol_subs = [
            ['H', 'HO'],
            ['H', 'OH'],
            ['O', 'HH']
        ]
        self.assertEqual(4, num_unique_subs(mol_subs, 'HOH'))

if __name__ == "__main__":
    unittest.main()

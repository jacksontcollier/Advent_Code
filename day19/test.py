#!/usr/bin/env python3

import unittest
import unittest.mock as mock
from day19 import MoleculeCalibrator

class ParsesMoleculeTransformCorrectly(unittest.TestCase):
    def test_one(self):
        expected = ("H", "HO")
        actual = MoleculeCalibrator.parse_mol_sub("H => HO")
        self.assertEqual(expected, actual)

    def test_two(self):
        expected = ("Al", "ThF")
        actual = MoleculeCalibrator.parse_mol_sub("Al => ThF")
        self.assertEqual(expected, actual)

    def test_three(self):
        expected = ("Al", "ThRnFAr")
        actual = MoleculeCalibrator.parse_mol_sub("Al => ThRnFAr")
        self.assertEqual(expected, actual)

class ParsesMoleculeFileCorrectly(unittest.TestCase):
    def test_one(self):
        test_data = "H => HO\nH => OH\n\nThRnFAr"
        expected_med_mol = "ThRnFAr"
        expected_mol_subs = [["H", "HO"], ["H", "OH"]]

        with mock.patch("builtins.open", mock.mock_open(read_data=test_data)):
            med_mol, mol_subs = MoleculeCalibrator.parse_mol_subs_file("test")
            self.assertEqual(expected_med_mol, med_mol)
            self.assertEqual(expected_mol_subs, mol_subs)

    def test_two(self):
        test_data = "H => HO\nH => OH\nO => HH\n\nOHOH"
        expected_med_mol = "OHOH"
        expected_mol_subs = [["H", "HO"], ["H", "OH"], ["O", "HH"]]

        with mock.patch("builtins.open", mock.mock_open(read_data=test_data)):
            med_mol, mol_subs = MoleculeCalibrator.parse_mol_subs_file("test")
            self.assertEqual(expected_med_mol, med_mol)
            self.assertEqual(expected_mol_subs, mol_subs)

class GeneratesSingleSubstitutionMoleculesCorrectly(unittest.TestCase):
    def test_one(self):
        med_mol = "HOH"
        mol_subs = ["H", "HO"]
        mol_cal = MoleculeCalibrator(med_mol, mol_subs)
        subs = mol_cal.single_subs(med_mol, mol_subs[0], mol_subs[1])
        self.assertEqual("HOOH", subs.__next__())

    def test_two(self):
        med_mol = "PBAlPRnFArCaCaAlBCaAlTiAlPMg"
        mol_subs = ["Al", "ThF"]
        mol_cal = MoleculeCalibrator(med_mol, mol_subs)

        expected = [
            "PBThFPRnFArCaCaAlBCaAlTiAlPMg",
            "PBAlPRnFArCaCaThFBCaAlTiAlPMg",
            "PBAlPRnFArCaCaAlBCaThFTiAlPMg",
            "PBAlPRnFArCaCaAlBCaAlTiThFPMg"
        ]

        expected_index = 0
        for sub in mol_cal.single_subs(med_mol, mol_subs[0], mol_subs[1]):
            self.assertEqual(expected[expected_index], sub)
            expected_index += 1

class CalculatesNumberOfUniqueSingleSubstitutions(unittest.TestCase):
    def test_one(self):
        med_mol = "HOH"
        mol_subs = [
            ["H", "HO"],
            ["H", "OH"],
            ["O", "HH"]
        ]
        mol_cal = MoleculeCalibrator(med_mol, mol_subs)
        expected = 4
        actual = mol_cal.num_unique_single_subs()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()

#! /usr/bin/env python3

from day19 import MoleculeCalibrator

mol_cal = MoleculeCalibrator.init_from_file('day19_input.txt')
print("Part 1 Answer: %d" % mol_cal.num_unique_single_subs())

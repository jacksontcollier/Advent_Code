#! /usr/bin/env python3

from day19 import parse_mol_file
from day19 import num_unique_subs

mol_subs, med_mol = parse_mol_file('day19_input.txt')
print("Part 1 Answer: %d" % num_unique_subs(mol_subs, med_mol))

#! /usr/bin/env python3

SUB_SYMBOL = "=>"

class MoleculeCalibrator:
    def __init__(self, med_mol, mol_subs):
        self.med_mol = med_mol
        self.mol_subs = mol_subs

    @staticmethod
    def parse_mol_sub(sub):
        token = sub.split(SUB_SYMBOL)
        preimage_mol = token[0].strip()
        image_mol = token[1].strip()
        return (preimage_mol, image_mol)

    @classmethod
    def parse_mol_subs_file(cls, mol_subs_file):
        mol_subs = []
        med_mol = ""
        done_reading_subs = False

        with open(mol_subs_file) as fin:
            for line in fin.readlines():
                line = line.strip()
                if done_reading_subs:
                    med_mol = line
                    break

                if line == "":
                    done_reading_subs = True
                    continue

                preimage_mol, image_mol = cls.parse_mol_sub(line)

                mol_subs.append([preimage_mol, image_mol])

        return (med_mol, mol_subs)

    @classmethod
    def init_from_file(cls, mol_subs_file):
        med_mol, mol_subs = cls.parse_mol_subs_file(mol_subs_file)
        return cls(med_mol, mol_subs)

    def make_sub(self, mol, pos, preimage_mol, image_mol):
        return mol[:pos] + mol[pos:].replace(preimage_mol, image_mol, 1)

    def single_subs(self, mol, preimage_mol, image_mol):
        pos = 0

        while pos < len(mol):
            pos = mol.find(preimage_mol, pos)
            if pos < 0:
                break
            yield self.make_sub(mol, pos, preimage_mol, image_mol)
            pos += 1

    def num_unique_single_subs(self):
        unique_subs = set()
        mol = self.med_mol

        for sub in self.mol_subs:
            for new_mol in self.single_subs(self.med_mol, sub[0], sub[1]):
                unique_subs.add(new_mol)

        return len(unique_subs)

    def get_inversed_mol_subs(self):
        inversed_mol_subs = []

        for sub in self.mol_subs:
            inversed_mol_subs.append([sub[1], sub[0]])

        return sorted(
            inversed_mol_subs,
            key=lambda sub: len(sub[0]) - len(sub[1]),
            reverse=True)

    def greedy_sub(self, mol, inversed_mol_subs, count):
        if mol == "e":
            if self.min_subs_single_electron < 0:
                self.min_subs_single_electron = count
            else:
                self.min_subs_single_electron = min(
                    self.min_subs_single_electron,
                    count)
            self.base_case_hits += 1
            return

        if self.base_case_hits > self.max_base_case_hits:
            return

        for sub in inversed_mol_subs:
            for new_mol in self.single_subs(mol, sub[0], sub[1]):
                self.greedy_sub(new_mol, inversed_mol_subs, count + 1)

    def get_min_subs_single_electron(self, max_base_case_hits):
        inversed_mol_subs = self.get_inversed_mol_subs()
        self.max_base_case_hits = max_base_case_hits
        self.base_case_hits = 0
        self.min_subs_single_electron = -1

        self.greedy_sub(self.med_mol, inversed_mol_subs, 0)

        return self.min_subs_single_electron


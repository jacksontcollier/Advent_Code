#! /usr/bin/env python3

TRANSFORMATION_SYMBOL = "=>"

def parse_molecule_transform(transformation_rule):
    token = transformation_rule.split(TRANSFORMATION_SYMBOL)
    from_molecule = token[0].strip()
    to_molecule = token[1].strip()
    return (from_molecule, to_molecule)

def parse_molecule_file(infile):
    molecule_map = dict()
    medicine_molecule = ""

    done_reading_substitutions = False 
    with open(infile) as fin: 
        for line in fin.readlines():
            line = line.strip() 
            if done_reading_substitutions:
                medicine_molecule = line
                break

            if line == "":
                done_reading_substitutions = True
                continue

            from_molecule, to_molecule = parse_molecule_transform(line)

            molecule_map[from_molecule] = to_molecule
            
    return (molecule_map, medicine_molecule) 


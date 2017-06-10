#! /usr/bin/env python3

SUB_SYMBOL = "=>"

def parse_mol_sub(sub):
    token = sub.split(SUB_SYMBOL)
    preimage_mol = token[0].strip()
    image_mol = token[1].strip()
    return (preimage_mol, image_mol)

def parse_mol_file(infile):
    mol_subs = []
    med_mol = ""
    done_reading_subs = False 
    
    with open(infile) as fin: 
        for line in fin.readlines():
            line = line.strip() 
            if done_reading_subs:
                med_mol = line
                break

            if line == "":
                done_reading_subs = True
                continue

            preimage_mol, image_mol = parse_mol_sub(line)

            mol_subs.append([preimage_mol, image_mol])
            
    return (mol_subs, med_mol) 

def num_unique_subs(mol_subs, mol):
    unique_subs = set()

    for sub in mol_subs:
        pos = 0
        while pos < len(mol):
            pos = mol.find(sub[0], pos)
            if pos < 0:
                break
            new_mol = mol[:pos] + mol[pos:].replace(sub[0], sub[1], 1)
            unique_subs.add(new_mol)
            pos += 1

    return len(unique_subs)


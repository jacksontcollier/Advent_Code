#!/usr/bin/env python3

import re

class Aunt_Sue:
    def __init__(self, data_entry):
        stats = [int(s) for s in re.findall(r'\d+', data_entry)]
        self.number = stats[0]
        del stats[0]
        
        self.properties = {}
        
        data_entry = data_entry.replace(":", "")
        data_entry = data_entry.replace("Sue", "")
        data_entry = data_entry.replace(",", "")
        data_entry = ''.join([i for i in data_entry if not i.isdigit()])
        
        props = data_entry.split()
        
        for i in range(len(props)):
            self.properties[props[i]] = stats[i]


def find_giftsending_aunt_sue(ticker_tape_aunt_sue, data_file, could_be_compare):
    with open(data_file) as fin:
        for line in fin.readlines():
            candidate = Aunt_Sue(line.rstrip())
            if could_be_compare(ticker_tape_aunt_sue, candidate):
                return candidate.number

    return 0

def could_be(ticker_tape_sue, different_sue):
    for prop in different_sue.properties.keys():
        if different_sue.properties[prop] != ticker_tape_sue.properties[prop]:
            return False

    return True

def could_be_retro(ticker_tape_sue, different_sue):
    for prop in different_sue.properties.keys():
        if prop == "cats" or prop == "trees":
            if different_sue.properties[prop] <= ticker_tape_sue.properties[prop]:
                return False
        elif prop == "pomeranians" or prop == "goldfish":
            if different_sue.properties[prop] >= ticker_tape_sue.properties[prop]:
                return False
        else:
            if different_sue.properties[prop] != ticker_tape_sue.properties[prop]:
                return False
    
    return True

#!/usr/bin/env python3

import re

class SantasList:
    def __init__(self, filename):
        self.filename = filename

    def count_differences(self):
        self.literal_total = 0
        self.inmemory_total = 0
        
        with open(self.filename, "r") as fin:
            for line in fin.readlines():
                line = line.rstrip()
                self.literal_total += len(line)
                line = line[1: len(line) - 1]
                for match in re.findall(r"\\\\", line): line = line.replace(match, "a")
                for match in re.findall(r"\\\"", line): line = line.replace(match, "a")
                for match in re.findall(r"\\x[0-9a-f]{2}", line): line = line.replace(match, "a")
                self.inmemory_total += len(line)

        print(self.literal_total - self.inmemory_total)

    def expand(self):
        self.original_total = 0
        self.expanded_total = 0

        with open(self.filename, "r") as fin:
            for line in fin.readlines():
                line = line.rstrip()
                self.original_total += len(line)
                self.expanded_total += len(line) + 2
                for c in line:
                    if (c == "\"") or (c == "\\"):
                        self.expanded_total += 1

        print(self.expanded_total - self.original_total)

annoying_list = SantasList("input_day08.txt") 
annoying_list.count_differences()
annoying_list.expand()

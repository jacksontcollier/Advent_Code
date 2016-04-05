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
                line = line.rstrip('\n')
                print(line)
                total = len(line) 
                self.literal_total += total
                print(line) 
                num_escaped_backslash = len(re.findall(r"\\\\", line))
                num_escaped_quote = len(re.findall(r"\\\"", line))
                num_escaped_hexnotation = len(re.findall(r"\\x[0-9a-fA-f]{2}", line))
                if line[0] == "\"": total -= 1
                if line[-1] == "\"": total -=1
                total -= num_escaped_backslash
                total -= num_escaped_quote
                total -= (3 * num_escaped_hexnotation)
                self.inmemory_total += total

        print(self.literal_total - self.inmemory_total)

        

list = SantasList("test001.txt") 
list.count_differences()

#!/usr/bin/env python3

import re
import itertools

class Person:
    def __init__(self, name):
        self.name = name
        self.likes = {}

    def add_like(self, name, units):
        self.likes[name] = units

    def favors_person(self, name):
        return self.likes[name]

class Table:
    def __init__(self, input_data):
        self.people = {}
        self.max_happiness = 0

        with open(input_data) as fin:
            for line in fin.readlines():
                fields = line.rstrip().replace('.','').split()
                amount = get_amount(line)
                
                if fields[0] in self.people:
                    p = self.people[fields[0]]
                else:
                    p = Person(fields[0])
                    self.people[p.name] = p

                p.add_like(fields[len(fields)-1], amount)
    
    def add_ambivalent_person(self, name):
        new_comer = Person(name)
        
        for p in self.people.keys():
            new_comer.add_like(p, 0)
            self.people[p].add_like(new_comer.name, 0)

        self.people[new_comer.name] = new_comer

    def calculate_max_happiness(self):
        seating_arrangements = list(itertools.permutations(self.people.keys()))
        
        for arrangement in seating_arrangements:
            happiness = 0 
            for i in range(len(arrangement)):
                left = arrangement[i-1] 
                right = arrangement[(i+1) % len(arrangement)]

                happiness += self.people[arrangement[i]].favors_person(left)
                happiness += self.people[arrangement[i]].favors_person(right)

            self.max_happiness = max(self.max_happiness, happiness)

        return self.max_happiness
                
def get_amount(s):
    amount = int(re.findall(r'\d+', s)[0])
    
    if 'lose' in s:
        amount *= -1

    return amount

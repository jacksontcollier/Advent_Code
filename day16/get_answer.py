#!/usr/bin/env python3

from day16 import Aunt_Sue
from day16 import find_giftsending_aunt_sue

ticker_tape_aunt_sue = None

with open('ticker_tape_aunt_sue.txt') as fin:
    for line in fin.readlines():
        ticker_tape_aunt_sue = Aunt_Sue(line.rstrip())

print("Answer 1: %d" % find_giftsending_aunt_sue(ticker_tape_aunt_sue, 'day16_input.txt'))

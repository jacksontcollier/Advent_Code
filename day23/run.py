#!/usr/bin/env python3
import sys
from machine import Machine

usage_message = (
    "./run.py part infile\n"
    "e.g. ...\n"
    "./run.py part-1 input.txt\n"
    "./run.py part-2 input.txt\n"
    "./run.py both input.txt\n"
)

if (len(sys.argv) != 3):
    print(usage_message)

if sys.argv[1] == "part-1":
    instructions = read_instructions_from_file(sys.argv[2])
    machine = Machine()
    machine.execute_program(instructions)
    print("Register: A --- Register B: " % (machine.register_a, machine.register_b))

#!/usr/bin/env python3
import sys
from machine import read_instructions_from_file
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

instructions = read_instructions_from_file(sys.argv[2])

if sys.argv[1] == "part-1" or sys.argv[1] == "both":
    machine = Machine()
    machine.execute_program(instructions)
    print("PART 1 ANSWER -- Register A: %d --- Register B: %d"
            % (machine.registers["a"], machine.registers["b"]))

if sys.argv[1] == "part-2" or sys.argv[1] == "both":
    machine = Machine(1)
    machine.execute_program(instructions)
    print("PART 2 ANSWER -- Register A: %d --- Register B: %d"
            % (machine.registers["a"], machine.registers["b"]))

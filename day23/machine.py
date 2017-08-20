#!/usr/bin/env python3
import math

def read_instructions_from_file(filename):
    instructions = []

    with open(filename) as fin:
        for line in fin.readlines():
            instructions.append(line.strip().replace(",", ""))

    return instructions

class Machine:
    def __init__(self):
        self.registers = { "a": 0, "b": 0 }
        self.pc = 0     # Program Counter
        self.executed_jmp_instruction = False
        self.isa_map = {
            "hlf": self.execute_hlf_instruction,
            "tpl": self.execute_hlf_instruction,
            "inc": self.execute_inc_instruction,
            "jmp": self.execute_jmp_instruction,
            "jie": self.execute_jie_instruction,
            "jio": self.execute_jio_instruction
        }

    def clear_registers(self):
        self.registers["a"] = 0
        self.registers["b"] = 0

    def get_register(self, register):
        return self.registers[register]

    def execute_instruction(self, instruction):
        instruction_tokens = instruction.split(" ")
        name = instruction_tokens[0]
        self.isa_map[name](*instruction_tokens[1:])

    def execute_hlf_instruction(self, register):
        result = math.floor(self.register_map[register] / 2)
        self.registers[register] = result

    def execute_tpl_instruction(self, register):
        result = self.registers[register] * 3;
        self.registers[register] = result

    def execute_inc_instruction(self, register):
        self.registers[register] += 1

    def execute_jmp_instruction(self, offset):
        self.pc += int(offset)
        self.executed_jmp_instruction = True

    def execute_jie_instruction(self, register, offset):
        if self.registers[register] % 2 == 0:
            self.pc += int(offset)
            self.executed_jmp_instruction = True

    def execute_jio_instruction(self, register, offset):
        if self.registers[register] % 2 == 1:
            self.pc += int(offset)
            self.executed_jmp_instruction = True

    def execute_program(self, program_instructions):
        self.clear_registers()
        self.pc = 0

        while self.pc < len(program_instructions) and self.pc >= 0:
            self.execute_instruction(program_instructions[self.pc])
            if self.executed_jmp_instruction == True:
                self.executed_jmp_instruction = False
            else:
                self.pc += 1


#!/usr/bin/env python3

from ctypes import *

class Circuit:
    def __init__(self, filename):
        self.Operations = ["AND", "OR", "LSHIFT", "RSHIFT",
                        "NOT"]
        self.wires = {}
 
        with open(filename, "r") as fin:
            instructions = fin.readlines()
            for command in instructions:
                self.parse_operation(command)

    def parse_operation(self, command):
        print("Command: %s" % command)
        print("=================")
        components = command.split("->")
        command_operation = "" 
        for operation in self.Operations:
            if operation in command:
                command_operation = operation
                if command_operation == "NOT":
                    operands = components[0].replace("NOT", "")
                    operands.strip(" ")
                else:
                    operands = components[0].split(command_operation)
        
        if command_operation == "":
            command_operation = "STORE"
            operands = components[0].rstrip()

        print("Command Operation: %s\n" % command_operation)
        print(operands)
        print(components[1])
        print("\n")

    def perform_operation(command_operation, operands, store_result):
        if command_operation != "STORE":
            if command_operation == "AND":
                first_operand = c_ushort(self.wires[operands[0].strip(' ')])
                second_operand = c_ushort(self.wires[operands[1].strip(' ')])
                result = c_ushort(first_operand & second_operand)
            elif command_operation == "OR":
                first_operand = c_ushort(self.wires[operands[0].strip(' ')])
                second_operand = c_ushort(self.wires[operands[1].strip(' ')])
                result = c_ushort(first_operand | second_operand)
            elif command_operation == "LSHIFT":
                first_operand = c_ushort(self.wires[operands[0].strip(' ')])
                second_operand = int(operands[1].strip(' '))
                result = c_ushort(first_operand << second_operand)
            elif command_operation == "RSHIFT":
                first_operand = c_ushort(self.wires[operands[0].strip(' ')])
                second_operand = int(operands[1].strip(' '))
                result = c_ushort(first_operand >> second_operand)
            elif command_operation == "NOT":
                first_operand = c_ushort(self.operands[1].strip(' '))
                result = c_ushort(~first_operand)
    
c = Circuit("test001.txt")

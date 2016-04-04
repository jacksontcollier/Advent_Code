#!/usr/bin/env python3

from ctypes import *
import re

class Circuit:
    def __init__(self, filename):
        self.Operations = ["AND", "OR", "LSHIFT", "RSHIFT",
                        "NOT"]
        self.Commands = []
        self.wires = {}
 
        with open(filename, "r") as fin:
            instructions = fin.readlines()
            for command in instructions:
                operation = ""
                for op in self.Operations:
                    if op in command:
                        operation = op
                if operation == "":
                    operation = "STORE"
                command = Command(command.replace("\n", ""), operation.replace(" ", ""), self.wires)
                self.Commands.append(command)
    
    def analyze(self):
        while (len(self.Commands)):
            for command in self.Commands:
             command.check_state()
             if command.can_execute:
                command.execute()
                self.Commands.remove(command)
       
    def print_commands(self):
        for command in self.Commands:
            command.print_state() 
                 
class Command:
    def __init__(self, command, operation, wires):
        self.command = command
        self.operation = operation
        self.wires = wires         
        self.components = self.command.split("->")
        self.num_operands = 0
        self.operands = []
        self.store_result_location = ""
        self.can_execute = False
        
        if self.operation == "NOT":
            operand = Operand(self.components[0].replace("NOT ", ""), self.wires)
            self.operands.append(operand)
            self.num_operands = 1
        elif self.operation == "STORE":
            operand = Operand(self.components[0].replace(" ", ""), self.wires)
            self.operands.append(operand)
            self.num_operands = 1
        else: 
            self.num_operands = 2
            left_side_operands = self.components[0].split(self.operation)
            operand = Operand(left_side_operands[0].replace(" ", ""), self.wires)
            self.operands.append(operand)
            operand = Operand(left_side_operands[1].replace(" ", ""), self.wires)
            self.operands.append(operand)

        self.store_result_location = self.components[1].replace(" ", "") 
    
    def execute(self):
        if self.operation == "STORE":
            self.wires[self.store_result_location] = c_ushort(operands[0].numeric_val)
        elif self.operation == "AND":
            self.wires[self.store_result_location] = c_ushort(operands[0].numeric_val & operands[1].numeric_val)
        elif self.operation == "OR":
            self.wires[self.store_result_location] = c_ushort(operands[0].numeric_val | operands[1].numeric_val)
        elif self.operation == "RSHIFT":
            self.wires[self.store_result_location] = c_ushort(operands[0].numeric_val >> operands[1].numeric_val)
        elif self.operation == "LSHIFT":
            self.wires[self.store_result_location] = c_ushort(operands[0].numeric_val << operands[1].numeric_val)
        elif self.operation == "NOT": 
            self.wires[self.store_result_lovation] = c_ushort(~operands[0].numeric_val)

    def check_state(self):
        for operand in self.operands:
            if not operand.check_numeric_value():
                return False
        
        return True
                
    def print_state(self):
        print("===========================================")
        print("Operation: %s --- Num Operands: %d --- Executable: %r" % (self.operation, self.num_operands, self.check_state()))
        print("    Operands: ")
        for op in self.operands:
            print("        Operand: %s --- Type: %s" % (op.val, op.val_type))
        print("Store Result in Location: %s" % (self.store_result_location))
        print()
                     
class Operand: 
    def __init__(self, operand, wires):
        self.val = operand
        self.has_numeric_val = False
        self.numeric_val = -1
        self.val_type = ""
        self.wires = wires

        if re.match("[a-zA-Z]", self.val) != None:
            self.val_type = "GATE_NAME"
        else:
            self.val_type = "NUMERIC_LITERAL"
            self.has_numeric_val = True
            self.numeric_val = int(self.val)
    
    def check_numeric_value(self):
        if self.has_numeric_val:
            return True
        if self.val in self.wires:
            self.numeric_val = int(self.wires[self.val])
        
        return False

circuit = Circuit("test001.txt")
circuit.print_commands()
circuit.analyze()
print(circuit.wires)

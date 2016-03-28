#!/usr/bin/env python3
# Jackson Collier

class Grid:
    def __init__(self, input_file, mode):
        self.M = [[0 for x in range(1000)] for x in range(1000)]
        self.toggle = "toggle"
        self.on = "turn on"
        self.off = "turn off"
        self.binary = False
        self.unbounded_above = False
 
        if mode == "binary":
            self.binary = True
        elif mode == "unbounded_above":
            self.unbounded_above = True
         
        self.input_file = input_file
        self.total_brightness = 0
 
        self.read_instructions(self.input_file)
    
    def read_instructions(self, input_file):
        fin = open(input_file)
        instruction_list = fin.readlines()

        for instruction in instruction_list:
            instruction.rstrip()
            self.parse_instruction(instruction)

        fin.close()

    def parse_instruction(self, instruction):
        tokens = instruction.split();
 
        if self.toggle in instruction:
            start = tokens[1].split(',')
            end = tokens[3].split(',')
            command = self.toggle
        else:
            start = tokens[2].split(',')
            end = tokens[4].split(',')
            if self.on in instruction:
                command = self.on
            else: 
                command = self.off
        
        self.execute_instruction(int(start[0]), int(start[1]), int(end[0]), int(end[1]), command)
        
    def execute_instruction(self, x1, y1, x2, y2, command):
        x_increment = (1 if (x1 <= x2) else -1) 
        y_increment = (1 if (y1 <= y2) else -1) 
        
        for i in range(x1, (x2 + 1), x_increment):
            for j in range (y1, (y2 + 1), y_increment):
                if command == self.toggle:
                    if self.binary: 
                        self.total_brightness += (1 if (self.M[i][j] == 0) else -1) 
                        self.M[i][j] = (self.M[i][j] + 1) % 2
                    elif self.unbounded_above:
                        self.total_brightness += 2
                        self.M[i][j] = self.M[i][j] + 2
                elif command == self.on:
                    if self.binary: 
                        self.total_brightness += (1 if (self.M[i][j] == 0) else 0)
                        self.M[i][j] = 1
                    elif self.unbounded_above:
                        self.total_brightness += 1
                        self.M[i][j] += 1
                else:
                    if self.binary:
                        self.total_brightness += (0 if (self.M[i][j] == 0) else -1)
                        self.M[i][j] = 0
                    elif self.unbounded_above:
                        self.total_brightness += (0 if (self.M[i][j] <= 0) else -1)
                        self.M[i][j] = (0 if (self.M[i][j] <= 0) else self.M[i][j] - 1)   

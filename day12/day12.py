#!/usr/bin/env python3

import re

def get_file_string(filename):
    file_string = "" 
    with open(filename) as fin:
        for line in fin.readlines():
            file_string += line.rstrip()

    return file_string

def json_sum(json_string):
    return sum([int(s) for s in re.findall(r'-?\d+', json_string)])

def json_remove_red(json_string):
    match = re.search(r'red', json_string)
    while match != None:
        i = match.span()[0] - 1
        
        openining_brace_index = -1
        closing_brace_index = -1
        
        inside_array = False
        inside_object = False
        
        open_objects = 0
        open_arrays = 0
        
        i = match.span()[1]

        # Decide whether inside array or object, if inside
        # object grab closing curly brace
        while i < len(json_string):
            if json_string[i] == '{':
                open_objects += 1    
            elif json_string[i] == '}':
                if open_objects == 0:
                    inside_object = True
                    closing_brace_index = i
                    break
                else:
                    open_objects -= 1
            
            if json_string[i] == '[':
                open_arrays += 1 
            elif json_string[i] == ']':
                if open_arrays == 0:
                    inside_array = True
                    break
                else:
                    open_arrays -= 1

            i += 1
        
        begin_slice = 0
        end_slice = 0
        
        if inside_array:
            begin_slice = match.span()[0]
            end_slice = match.span()[1] 
        else:
            # Grab opening curly brace
            i = match.span()[0] - 1
            close_objects = 0
            
            while i >= 0:
                if json_string[i] == '}':
                    close_objects += 1
                elif json_string[i] == '{':
                    if close_objects == 0:
                        opening_brace_index = i
                        break
                    else:
                        close_objects -= 1

                i -= 1
            
            begin_slice = opening_brace_index
            end_slice = closing_brace_index + 1

        json_string = json_string[:begin_slice] + json_string[end_slice:]
        
        match = re.search(r'red', json_string)
    
    return json_string

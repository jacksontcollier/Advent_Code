#!/usr/bin/env python3
# Jackson Collier

from hashlib import md5

def generate_input(hash_input, num_zeros):
    zero_string = ""

    for i in range (0, num_zeros):
        zero_string += str(0) 

    i = 0
    while True:
        m = md5((hash_input + str(i)).encode('utf-8'))	        

        if str(m.hexdigest())[0:num_zeros] == zero_string:
            return i

        i += 1

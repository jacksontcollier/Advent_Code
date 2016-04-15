#!/usr/bin/env python3

def look(digits):
    # sentinelize digits 
    digits += "*"
    consecutive_digits = []
    current_digit = digits[0]
    i = 1
    subsequence = ""
    subsequence += current_digit
    
    while (i < len(digits)):
        if digits[i] != current_digit:
            consecutive_digits.append(subsequence)
            current_digit = digits[i]
            subsequence = ""
            subsequence += current_digit
        else:
            subsequence += digits[i]

        i += 1 

    return consecutive_digits

def say(consec_digits):
    new_say_sequence = ""
    for sequence in consec_digits:
        new_say_sequence += (str(len(sequence)) + str(sequence[0]))

    return new_say_sequence

def look_and_say(digits):
    return say(look(digits))

def repeated_look_and_say_length(digits, num_times):
    for i in range(num_times):
        digits = look_and_say(digits)

    return len(digits)

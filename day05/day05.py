#!/usr/bin/env python3
# Jackson Collier
# Solution for both parts of Advent of Code exercise, day 5.

# ======================================================= #
# class representing constraints for first half of day 5

class FirstConstraints:
    
    # Members match constraints of first half of day 5
    def __init__(self):
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.disallowed_strings = ['ab', 'cd', 'pq', 'xy']
    
    # pass string as argument to instance of class, will return
    # "naughty" or "nice"
    def naughty_or_nice(self, s):
        if self.num_vowels(s) < 3:
            return "naughty"

        if not self.contains_double_letter(s):
            return "naughty"

        if self.contains_disallowed_string(s):
            return "naughty"

        return "nice"
    
    # pass string 's' as arg. returns number of 
    # vowels (a, e, i, o, u) in s
    def num_vowels(self, s):
        num_vowels = 0    
        
        for c in s:
            if c in self.vowels:
                num_vowels += 1

        return num_vowels
    
    # pass string 's' as arg. returns True if 
    # s contains two adjacent,    equal characters
    def contains_double_letter(self, s):
        i = 0
        while i < (len(s) - 1):
            if s[i] == s[i+1]:
                return True
            i += 1

        return False
    
    # pass string 's' as arg. returns True if 
    # s contains any of strings in member 'disallowed strings'
    def contains_disallowed_string(self, s):
        for disallowed in self.disallowed_strings:
            if disallowed in s:
                return True
        
        return False

# ======================================================= #
# class representing constraints for second half of day 5

class SecondConstraints:
    
    # pass string 's' as an arg, will return naughty or nice    
    def naughty_or_nice(self, s):
        if not self.has_two_pair(s):
            return "naughty"

        if not self.has_three_char_palindrome(s):
            return "naughty"

        return "nice"
    
    # pass string 's' as an arg, returns True if
    # s has two nonoverlapping equal substrings of 
    # length 2
    def has_two_pair(self, s):
        i = 0

        while (i + 1) < len(s):
            j = i + 2
            while (j + 1) < len(s):
                if s[i:(i+2)] == s[j:(j+2)]:
                    return True
                j += 1
            i += 1    
        

        return False
    
    # pass string 's' as an arg, returns True if
    # s contains a three character palindrome
    def has_three_char_palindrome(self, s):
        i = 1
        while (i + 1) < len(s):
            if s[i-1] == s[i+1]:
                return True
            
            i += 1
        
        return False     

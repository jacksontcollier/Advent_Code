#!/usr/bin/env python3

from enum import Enum

class Password:
    def __init__(self, orig_passwd):
        self.orig_passwd = orig_passwd
        self.numeric_vals = []

        for c in self.orig_passwd:
            self.numeric_vals.append(ord(c) - 97)

    def increment(self):
        overflow = True
        index = len(self.numeric_vals) - 1
        alphabet_len = 26

        while overflow:
            if self.numeric_vals[index] == (alphabet_len - 1):
                if index == 0:
                    self.reset()
                    return
                overflow = True
                self.numeric_vals[index] = (self.numeric_vals[index] + 1) % alphabet_len
                index -= 1
            else:
                self.numeric_vals[index] = (self.numeric_vals[index] + 1) % alphabet_len
                overflow = False

    def reset(self):
        for i in range(len(self.numeric_vals)):
            self.numeric_vals[i] = 0

    def get_string(self):
        s = ""
        for val in self.numeric_vals:
            s += chr(val + ord('a'))

        return s

    def contains_three_straight(self):
        for i in range(len(self.numeric_vals) - 2):
            a = self.numeric_vals[i]
            b = self.numeric_vals[i+1]
            c = self.numeric_vals[i+2]

            if ((a + 1) == b) and ((b + 1) == c):
                return True

        return False

    def excludes_unallowed(self):
        for val in self.numeric_vals:
            c = chr(val + ord('a'))
            if (c == 'i') or (c == 'o') or (c == 'l'):
                return False

        return True

    def contains_pair_nonoverlapping(self):
        for i in range(len(self.numeric_vals) - 1):
            if self.numeric_vals[i] == self.numeric_vals[i+1]:
                j = i + 2
                while j < (len(self.numeric_vals) - 1):
                    if self.numeric_vals[j] == self.numeric_vals[j+1]:
                        return True
                    j += 1

        return False

    def is_valid(self):
        contains_three = self.contains_three_straight()
        excludes = self.excludes_unallowed()
        contains_pair = self.contains_pair_nonoverlapping()

        if contains_three and excludes and contains_pair:
            return True

        return False

    def get_next_password(self):
        while not self.is_valid():
            self.increment()

        return self.get_string()

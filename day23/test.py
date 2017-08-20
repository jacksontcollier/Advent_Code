#!/usr/bin/env python3

import unittest
import unittest.mock as mock
from machine import read_instructions_from_file
from machine import Machine

class ReadsInstructionsFromFileCorrectly(unittest.TestCase):
    def test_one(self):
        test_data = "inc a\njio a, +2\ntpl a\ninc a\n"
        expected = ["inc a", "jio a +2", "tpl a", "inc a"]

        with mock.patch("builtins.open", mock.mock_open(read_data=test_data)):
            actual = read_instructions_from_file("test")
            self.assertEqual(expected, actual)

class MachineExecutesProgramCorrectly(unittest.TestCase):
    def test_one(self):
        test_data = "inc a\njio a, +2\ntpl a\ninc a\n"

        with mock.patch("builtins.open", mock.mock_open(read_data=test_data)):
            instructions = read_instructions_from_file("test")
            machine = Machine()
            machine.execute_program(instructions)
            self.assertEqual(2, machine.get_register("a"))

if __name__ == "__main__":
    unittest.main()

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

class ExecuteInstructionCallsCorrectInstructionHandler(unittest.TestCase):
    def test_one(self):
        with mock.patch.object(Machine, "execute_hlf_instruction") as mock_method:
            vm = Machine()
            vm.execute_instruction("hlf a")

        mock_method.assert_called_with("a")

        with mock.patch.object(Machine, "execute_tpl_instruction") as mock_method:
            vm = Machine()
            vm.execute_instruction("tpl a")

        mock_method.assert_called_with("a")

        with mock.patch.object(Machine, "execute_inc_instruction") as mock_method:
            vm = Machine()
            vm.execute_instruction("inc a")

        mock_method.assert_called_with("a")

        with mock.patch.object(Machine, "execute_jmp_instruction") as mock_method:
            vm = Machine()
            vm.execute_instruction("jmp +23")

        mock_method.assert_called_with("+23")

        with mock.patch.object(Machine, "execute_jie_instruction") as mock_method:
            vm = Machine()
            vm.execute_instruction("jie a +4")

        mock_method.assert_called_with("a", "+4")

        with mock.patch.object(Machine, "execute_jio_instruction") as mock_method:
            vm = Machine()
            vm.execute_instruction("jio a +19")

        mock_method.assert_called_with("a", "+19")

if __name__ == "__main__":
    unittest.main()

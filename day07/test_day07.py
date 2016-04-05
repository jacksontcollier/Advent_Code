#!/usr/bin/env python3

import unittest
from ctypes import *
from day07 import *

class TestLogicCircuit(unittest.TestCase):
    def test_one(self):
        circuit = Circuit("test001.txt", "")
        circuit.analyze()
        self.assertEqual(c_ushort(circuit.wires['d']).value, c_ushort(72).value) 

    def test_two(self):
        circuit = Circuit("test001.txt", "")
        circuit.analyze()
        self.assertEqual(c_ushort(circuit.wires['e']).value, c_ushort(507).value) 

    def test_three(self):
        circuit = Circuit("test001.txt", "")
        circuit.analyze()
        self.assertEqual(c_ushort(circuit.wires['f']).value, c_ushort(492).value) 

    def test_four(self):
        circuit = Circuit("test001.txt", "")
        circuit.analyze()
        self.assertEqual(c_ushort(circuit.wires['g']).value, c_ushort(114).value) 

    def test_five(self):
        circuit = Circuit("test001.txt", "")
        circuit.analyze()
        self.assertEqual(c_ushort(circuit.wires['h']).value, c_ushort(65412).value) 

    def test_six(self):
        circuit = Circuit("test001.txt", "")
        circuit.analyze()
        self.assertEqual(c_ushort(circuit.wires['i']).value, c_ushort(65079).value)

    def test_seven(self):
        circuit = Circuit("test001.txt", "")
        circuit.analyze()
        self.assertEqual(c_ushort(circuit.wires['x']).value, c_ushort(123).value)

    def test_eight(self):
        circuit = Circuit("test001.txt", "")
        circuit.analyze()
        self.assertEqual(c_ushort(circuit.wires['y']).value, c_ushort(456).value)
    
    def test_nine(self):
        circuit = Circuit("day07_input.txt", "")
        circuit.analyze()
        self.assertEqual(c_ushort(circuit.wires['a']).value, c_ushort(16076).value)

    def test_ten(self):
        circuit = Circuit("day07_input.txt", "")
        circuit.analyze()
        result = circuit.wires['a']
        circuit = Circuit("day07_input.txt", "b")
        circuit.wires["b"] = result
        circuit.analyze()
        self.assertEqual(c_ushort(circuit.wires['a']).value, c_ushort(2797).value)

if __name__ == '__main__':
    unittest.main()

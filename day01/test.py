import unittest

from elevator import count_floors
from elevator import get_position

class TestCountFloors(unittest.TestCase):
    
    def test_one(self):
        self.assertEqual(count_floors('(())'), 0)

    def test_two(self):
        self.assertEqual(count_floors('()()'), 0)

    def test_three(self):
        self.assertEqual(count_floors('((('), 3)

    def test_four(self):
        self.assertEqual(count_floors('(()(()('), 3)

    def test_five(self):
        self.assertEqual(count_floors('))((((('), 3)

    def test_six(self):
        self.assertEqual(count_floors('())'), -1)

    def test_seven(self):
        self.assertEqual(count_floors('))('), -1)

    def test_eight(self):
        self.assertEqual(count_floors(')))'), -3)

    def test_nine(self):
        self.assertEqual(count_floors(')())())'), -3)

    def test_ten(self):
        input_file = open("advent_test_one.txt")
        
        directions = ""
        direction_lines = input_file.readlines()
        
        for line in direction_lines:
            line.rstrip('\n')
            directions += line

        input_file.close()

        self.assertEqual(count_floors(directions), 74)

    def test_eleven(self):
        self.assertEqual(get_position(')'), 1)

    def test_twelve(self):
        self.assertEqual(get_position('()())'), 5)

    def test_thirteen(self):
        input_file = open("advent_test_two.txt")

        directions = ""
        direction_lines = input_file.readlines()

        for line in direction_lines:
            line.rstrip('\n')
            directions += line
        
        input_file.close()

        self.assertEqual(get_position(directions), 1795)

if __name__ == '__main__':
    unittest.main()

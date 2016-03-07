import unittest

from delivery import count_houses
from delivery import robo_count

def grab_input(input_file):
    fin = open(input_file)
    
    directions = ""
    direction_lines = fin.readlines()

    for line in direction_lines:
        line.rstrip()
        directions += line

    fin.close()

    return directions

class TestHouseCount(unittest.TestCase):
    
    def test_one(self):
        self.assertEqual(count_houses('<'), 2)

    def test_two(self):
        self.assertEqual(count_houses('^>v<'), 4)

    def test_three(self):
        self.assertEqual(count_houses('^v^v^v^v^v'), 2)

    def test_four(self):
        self.assertEqual(count_houses(grab_input("advent_test_one.txt")), 2081) 

    def test_five(self):
        self.assertEqual(robo_count('^v'), 3)
    
    def test_six(self):
        self.assertEqual(robo_count('^>v<'), 3)

    def test_seven(self):
        self.assertEqual(robo_count('^v^v^v^v^v'), 11)

    def test_eight(self):
        print  "Answer Two: %d" % robo_count(grab_input("advent_test_two.txt"))

if __name__ == '__main__':
    unittest.main()

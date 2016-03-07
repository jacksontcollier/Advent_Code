import unittest

from presents import calc_required_paper
from presents import calc_required_ribbon

def create_presents_array(input_file):
    fin = open(input_file)
    
    presents = []
    
    present_lines = fin.readlines()

    for line in present_lines:
        line.rstrip()
        presents.append(line)

    return presents

class TestWrappingPaperCalculations(unittest.TestCase):
    
    def test_one(self):
        presents_list = create_presents_array("paper_test_001.txt")
        self.assertEqual(calc_required_paper(presents_list), 58)

    def test_two(self):
        presents_list = create_presents_array("paper_test_002.txt")
        self.assertEqual(calc_required_paper(presents_list), 43)

    def test_three(self):
        presents_list = create_presents_array("paper_test_003.txt")
        self.assertEqual(calc_required_paper(presents_list), 101)

    def test_four(self):
        presents_list = create_presents_array("advent_test_one.txt")
        self.assertEqual(calc_required_paper(presents_list), 1606483) 

class TestRibbonCalculations(unittest.TestCase):
    
    def test_one(self):
        presents_list = create_presents_array("ribbon_test_001.txt")
        self.assertEqual(calc_required_ribbon(presents_list), 34)

    def test_two(self):
        presents_list = create_presents_array("ribbon_test_002.txt")
        self.assertEqual(calc_required_ribbon(presents_list), 14)

    def test_three(self):
        presents_list = create_presents_array("ribbon_test_003.txt")
        self.assertEqual(calc_required_ribbon(presents_list), 48)

    def test_four(self):
        presents_list = create_presents_array("advent_test_one.txt")
        print "Part Two Answer: %d\n" % calc_required_ribbon(presents_list)

if __name__== '__main__':
    unittest.main()

#!/usr/bin/env python3

import unittest
from combinations import combination
from item import Item
from fighter import Fighter
from battle import Battle
from minimal_expense import item_selection
from minimal_expense import get_minimal_expense

test_items = [
    Item("Option #1", 1, 2, 3),
    Item("Option #2", 3, 5, 0),
    Item("Option #3", 3, 0, 1),
    Item("Option #4", 2, 4, 1),
    Item("Option #5", 5, 2, 0)
]

class GeneratesCombinationsCorrectly(unittest.TestCase):
    def test_one(self):
        expected = []
        combinations = combination(test_items, 0, 0)
        self.assertEqual(expected, combinations.__next__())

    def test_two(self):
        for index, combo in enumerate(combination(test_items, 1, 0)):
            expected = [test_items[index]]
            self.assertEqual(expected, combo)

    def test_three(self):
        combos = combination(test_items, 2, 0)

        expected = [test_items[0], test_items[1]]
        self.assertEqual(expected, combos.__next__())
        expected = [test_items[0], test_items[2]]
        self.assertEqual(expected, combos.__next__())
        expected = [test_items[0], test_items[3]]
        self.assertEqual(expected, combos.__next__())
        expected = [test_items[0], test_items[4]]
        self.assertEqual(expected, combos.__next__())

        expected = [test_items[1], test_items[2]]
        self.assertEqual(expected, combos.__next__())
        expected = [test_items[1], test_items[3]]
        self.assertEqual(expected, combos.__next__())
        expected = [test_items[1], test_items[4]]
        self.assertEqual(expected, combos.__next__())

        expected = [test_items[2], test_items[3]]
        self.assertEqual(expected, combos.__next__())
        expected = [test_items[2], test_items[4]]
        self.assertEqual(expected, combos.__next__())

        expected = [test_items[3], test_items[4]]
        self.assertEqual(expected, combos.__next__())

class CalculateItemSelectionCorrectly(unittest.TestCase):
    def test_one(self):
        selection = item_selection(test_items, 0, 2)
        expected = []
        self.assertEqual(expected, selection.__next__())

        expected = [test_items[0]]
        self.assertEqual(expected, selection.__next__())
        expected = [test_items[1]]
        self.assertEqual(expected, selection.__next__())
        expected = [test_items[2]]
        self.assertEqual(expected, selection.__next__())
        expected = [test_items[3]]
        self.assertEqual(expected, selection.__next__())
        expected = [test_items[4]]
        self.assertEqual(expected, selection.__next__())

        expected = [test_items[0], test_items[1]]
        self.assertEqual(expected, selection.__next__())
        expected = [test_items[0], test_items[2]]
        self.assertEqual(expected, selection.__next__())
        expected = [test_items[0], test_items[3]]
        self.assertEqual(expected, selection.__next__())
        expected = [test_items[0], test_items[4]]
        self.assertEqual(expected, selection.__next__())
        expected = [test_items[1], test_items[2]]
        self.assertEqual(expected, selection.__next__())
        expected = [test_items[1], test_items[3]]
        self.assertEqual(expected, selection.__next__())
        expected = [test_items[1], test_items[4]]
        self.assertEqual(expected, selection.__next__())
        expected = [test_items[2], test_items[3]]
        self.assertEqual(expected, selection.__next__())
        expected = [test_items[2], test_items[4]]
        self.assertEqual(expected, selection.__next__())
        expected = [test_items[3], test_items[4]]
        self.assertEqual(expected, selection.__next__())

class CalculateBattleWinnerCorrectly(unittest.TestCase):
    def test_one(self):
        hero = Fighter("Hero", 8)
        hero.set_attack(5)
        hero.set_armor(5)

        boss = Fighter("Boss", 12)
        boss.set_attack(7)
        boss.set_armor(2)

        battle = Battle(hero, boss)
        battle.start()
        expected = hero
        actual = battle.get_winner()
        self.assertEqual(expected, actual)

class CalculatesPartOneAnswerCorrectly(unittest.TestCase):
    def test_one(self):
        expected = 91
        actual = get_minimal_expense(100, 2, 8)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()

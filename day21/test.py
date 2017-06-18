#!/usr/bin/env python3

import unittest
from weapon import weapon_options
from combinations import combination
from fighter import Fighter
from battle import Battle

class GeneratesCombinationsCorrectly(unittest.TestCase):
    def test_one(self):
        expected = []
        combinations = combination(weapon_options, 0, 0)
        self.assertEqual(expected, combinations.__next__())

    def test_two(self):
        for index, combo in enumerate(combination(weapon_options, 1, 0)):
            expected = [weapon_options[index]]
            self.assertEqual(expected, combo)

    def test_three(self):
        combos = combination(weapon_options, 2, 0)

        expected = [weapon_options[0], weapon_options[1]]
        self.assertEqual(expected, combos.__next__())
        expected = [weapon_options[0], weapon_options[2]]
        self.assertEqual(expected, combos.__next__())
        expected = [weapon_options[0], weapon_options[3]]
        self.assertEqual(expected, combos.__next__())
        expected = [weapon_options[0], weapon_options[4]]
        self.assertEqual(expected, combos.__next__())

        expected = [weapon_options[1], weapon_options[2]]
        self.assertEqual(expected, combos.__next__())
        expected = [weapon_options[1], weapon_options[3]]
        self.assertEqual(expected, combos.__next__())
        expected = [weapon_options[1], weapon_options[4]]
        self.assertEqual(expected, combos.__next__())

        expected = [weapon_options[2], weapon_options[3]]
        self.assertEqual(expected, combos.__next__())
        expected = [weapon_options[2], weapon_options[4]]
        self.assertEqual(expected, combos.__next__())

        expected = [weapon_options[3], weapon_options[4]]
        self.assertEqual(expected, combos.__next__())

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

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3

import unittest
from day15 import Ingredient
from day15 import Recipe

class CalculatesBestCookieScoreCorrectly(unittest.TestCase):
    def test_one(self):
        cookie_recipe = Recipe('input_001.txt')
        cookie_recipe.make_best_cookie_recipe()
        self.assertEqual(62842880, cookie_recipe.best_cookie_score)

    def test_two(self):
        cookie_recipe = Recipe('input_001.txt')
        cookie_recipe.add_calories_restriction(500) 
        cookie_recipe.make_best_cookie_recipe()
        self.assertEqual(57600000, cookie_recipe.best_cookie_score) 

if __name__=='__main__':
    unittest.main()

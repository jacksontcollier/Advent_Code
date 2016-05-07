#!/usr/bin/env python3

from day15 import Ingredient
from day15 import Recipe

r = Recipe('input_day15.txt')
r.make_best_cookie_recipe()
print("Part 1 answer: %d" % r.best_cookie_score)

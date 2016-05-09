#!/usr/bin/env python3

import re
import sys

class Ingredient:
    def __init__(self, ingredient_listing):
        self.name = ingredient_listing.split(':')[0]
        properties = [int(s) for s in re.findall(r'-?\d+',  ingredient_listing)]
        self.capacity = properties[0]
        self.durability = properties[1]
        self.flavor = properties[2]
        self.texture = properties[3]
        self.calories = properties[4]

class Recipe:
    def __init__(self, ingredient_file):
        self.ingredients = []
        self.amounts = []
        self.best_cookie_score = 0
        self.restrict_calories = False
        self.calories_restriction = -1

        with open(ingredient_file) as fin:
            for line in fin.readlines():
                self.ingredients.append(Ingredient(line.rstrip()))
                self.amounts.append(0)
    
    def add_calories_restriction(self, restriction):
        self.calories_restriction = restriction
        self.restrict_calories = True

    def make_best_cookie_recipe(self):
        self.choose_ingredient_amount(0, 100)

    def choose_ingredient_amount(self, ingredient_index, teaspoons_available):
        if ingredient_index + 1 == len(self.ingredients):
            self.amounts[ingredient_index] = teaspoons_available
            self.calculate_recipe_value()
            return

        for i in range(teaspoons_available):
            self.amounts[ingredient_index] = i
            self.choose_ingredient_amount(ingredient_index + 1, teaspoons_available - i)

    def calculate_recipe_value(self):
        total_capacity = 0
        total_durability = 0
        total_flavor = 0
        total_texture = 0
        total_calories = 0

        for i in range(len(self.ingredients)):
            total_capacity += (self.ingredients[i].capacity * self.amounts[i])
            total_durability += (self.ingredients[i].durability * self.amounts[i])
            total_flavor += (self.ingredients[i].flavor * self.amounts[i])
            total_texture += (self.ingredients[i].texture * self.amounts[i])
            total_calories += (self.ingredients[i].calories * self.amounts[i])

        total_capacity = max(0, total_capacity)
        total_durability = max(0, total_durability)
        total_flavor = max(0, total_flavor)
        total_texture = max(0, total_texture)

        recipe_score = total_capacity * total_durability * total_flavor * total_texture
        
        if (self.restrict_calories and (self.calories_restriction == total_calories)) \
                or not self.restrict_calories:
            self.best_cookie_score = max(self.best_cookie_score, recipe_score)

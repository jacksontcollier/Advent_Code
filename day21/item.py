#!/usr/bin/env python3
class Item:
    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def get_damage(self):
        return self.damage

    def get_armor(self):
        return self.armor

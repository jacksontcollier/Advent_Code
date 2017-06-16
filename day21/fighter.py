#!/usr/bin/env

class Fighter:
    def __init__(self, name, hit_points):
        self.name = name
        self.hit_points
        self.armor = 0
        self.attack = 0

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_hit_points(self):
        return self.hit_points

    def set_hit_points(self, hit_points):
        self.hit_point = hit_points

    def get_armor(self):
        return self.armor

    def set_armor(self, armor):
        self.armor = armor

    def get_attack(self):
        return self.attack

    def set_attack(self, attack):
        self.attack = attack

    def is_dead(self):
        return self.hit_points <= 0

    def damage(self, damage):
        self.hit_points -= damage

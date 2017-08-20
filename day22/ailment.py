#!/usr/bin/env python3

class Ailment:
    def __init__(self, name, duration, hp_augment):
        self.name = name
        self.duration = duration
        self.hp_augment = hp_augment

    def decrement_duration(self):
        self.duration = max(0, self.duration - 1)

    def get_hp_augment(self):
        return self.hp_augment

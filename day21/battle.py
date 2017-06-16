#!/usr/bin/env python3

class Battle:
    def __init__(self, attacker, defender)
        self.attacker = attacker
        self.defender = defender
        self.winner = None

    def start(self):
        while True:
            damage = max(1, attacker.get_attack() - defender.get_armor())
            self.defender.damage(damage)

            if self.defender.is_dead():
                self.winner = self.attacker
                return

            damage = max(1, defender.get_attack() - attacker.get_armor())
            self.attacker.damage(damage)

            if self.attacker.is_dead():
                self.winner = self.defender
                return

    def get_winner(self):
        return self.winner


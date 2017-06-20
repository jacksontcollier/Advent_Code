#!/usr/bin/env python3

class Battle:
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender
        self.winner = None

    def execute_turn(self, attacker, defender):
        damage = max(1, attacker.get_attack() - defender.get_armor())
        defender.damage(damage)

        if defender.is_dead():
            self.winner = attacker

    def start(self):
        while True:
            self.execute_turn(self.attacker, self.defender)
            if self.winner != None:
                return
            self.execute_turn(self.defender, self.attacker)
            if self.winner != None:
                return

    def get_winner(self):
        return self.winner


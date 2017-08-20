#usr/bin/env python3

class Fighter:
    def __init__(self, name, hp, armor, attack):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.armor = armor
        self.attack = attack
        self.effects = []

    def get_attack(self):
        return self.attack

    def get_armor(self):
        return self.armor

    def decrease_hp(self, decrease):
        self.hp = max(0, self.hp - damage)

    def increase_hp(self, increase):
        self.hp = max(self.max_hp, self.hp + increase)

    def attack(self, opponent):
        attack_damage = self.get_attack()
        opponent_armor = opponent.get_armor()
        damage_dealt = max(1, attack_damage - opponent_armor)
        opponent.deal_damage(damage_dealt)

    def has_active_effect(self, effect):
        for active_effect in self.effects:
            if active_effect.name == effect.name:
                return True

        return False

    def register_ailment(self, ailment):
        self.ailments.append(ailment)

    def apply_ailments(self):
        for ailment in self.ailments:
            ailment.apply(self)

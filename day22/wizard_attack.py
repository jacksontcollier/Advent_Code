class WizardAttack:
    def __init__(self, name, mana_cost, perform):
        self.name = name
        self.mana_cost = mana_cost
        self.perform = perform

    def get_name(self):
        return self.name

    def get_mana_cost(self):
        return self.mana_cost

def perform_magic_missile(wizard, opponent):
    MAGIC_MISSILE_MANA_COST = 53
    MAGIC_MISSILE_DAMAGE = 4

    if (wizard.get_mana >= MAGIC_MISSILE_MANA_COST):
        opponent.deal_damage(MAGIC_MISSILE_DAMAGE)
        wizard.decrement_mana(MAGIC_MISSILE_MANA_COST)

    return

def perform_drain(wizard, opponent):
    DRAIN_MANA_COST = 73
    DRAIN_DAMAGE = 2
    DRAIN_HP_ABSORB = 2

    if (wizard.get_mana >= DRAIN_MANA_COST)
        opponent.deal_damage(DRAIN_DAMAGE)
        wizard.increase_hp(DRAIN_HP_ABSORB)

def perform_shield(wizard, opponent):
    SHIELD_MANA_COST = 113
    SHIELD_TURN_DURATION = 6
    SHIELD_ARMOR_INCREASE = 7

    if (wizard.get_mana >= SHIELD_MANA_COST):

    can_cast_shield = true

    if (w


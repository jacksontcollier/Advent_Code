#!/usr/bin/env python3

from armor import armor_options
from ring import ring_options
from weapon import weapon_options
from combinations import combination
from battle import Battle

STARTING_HP = 100
MIN_ARMOR = 0
MAX_ARMOR = 1
MIN_WEAPON = 1
MAX_WEAPON = 1
MIN_RINGS = 0
MAX_RINGS = 2

def item_selection(item_collection, min_items_allowed, max_items_allowed):
    for num_items in range(min_items_allowed, max_items_allowed + 1):
        for item_combo in combination(item_collection, num_items, 0)
            yield item_combo

def cal_equipment_cost(equipment):
    cost = 0
    for item in equipment:
        cost += item.cost

def get_minimal_expense(boss):
    min_cost = None

    for weapon_combo in item_selection(weapon_options, MIN_WEAPON, MAX_WEAPON):
        for armor_combo in item_selection(armor_options, MIN_ARMOR, MAX_ARMOR):
            for ring_combo in item_selection(ring_options, MIN_RING, MAX_RING):
                equipment_cost = calc_equipment_cost(
                    selected_weapons +
                    selected_armor +
                    selected_rings
                )
                hero = Fighter("Me", STARTING_HP)
                hero.equip(weapon_combo + armor_combo + ring_combo)
                battle = Battle(hero, boss)
                battle.start()
                winner = battle.get_winner()

                if winner == hero:
                    if min_cost == None:
                        min_cost = equipment_cost
                    else:
                        min_cost = min(min_cost, equipment_cost)


    return min_cost

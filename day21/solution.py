#!/usr/bin/env python3

from minimal_expense import get_minimal_expense

BOSS_HP = 100
BOSS_DAMAGE = 8
BOSS_ARMOR = 2

min_expense = get_minimal_expense(BOSS_HP, BOSS_ARMOR, BOSS_DAMAGE)
print("1st part answer: %d" % min_expense)

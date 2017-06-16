#!/usr/bin/env python3

from item import Item

weapons = [
    Item("Dagger", 8, 4, 0),
    Item("Shortsword", 10, 5, 0),
    Item("Warhammer", 25, 6, 0),
    Item("Longsword", 40, 7, 0),
    Item("Greataxe", 74, 8, 0)
]

def combination(collection, num_combinations, index):
    if num_combinations == 0:
        yield []

    for i in range(index, len(collection)):
        for combo in combination(collection, num_combinations - 1, i + 1):
            yield [collection[i]] + combo


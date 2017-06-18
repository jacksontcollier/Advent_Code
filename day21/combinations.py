#!/usr/bin/env python3

def combination(collection, num_combinations, index):
    if num_combinations == 0:
        yield []

    for i in range(index, len(collection)):
        for combo in combination(collection, num_combinations - 1, i + 1):
            yield [collection[i]] + combo


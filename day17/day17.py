#!/usr/bin/env python3

import itertools

def read_container_file(filename):
    container_sizes = []

    with open(filename) as fin:
        for line in fin.readlines():
            container_sizes.append(int(line.rstrip()))

    return container_sizes

def get_valid_combinations(container_sizes, eggnog_amount):
    valid_container_combinations = []

    for i in range(1, len(container_sizes) + 1):
        container_combinations = list(itertools.combinations(container_sizes, i))
        for combo in container_combinations:
            if sum(combo) == eggnog_amount:
                valid_container_combinations.append(combo)

    return valid_container_combinations

def count_valid_combinations(container_sizes, eggnog_amount):
    return len(get_valid_combinations(container_sizes, eggnog_amount))

def count_min_container_combo(container_sizes, eggnog_amount):
    container_combinations = get_valid_combinations(container_sizes, eggnog_amount)

    min_containers_needed = -1
    num_min_combos = 0
    for combo in container_combinations:
        if (min_containers_needed == -1) or (len(combo) < min_containers_needed): 
            min_containers_needed = len(combo)
            num_min_combos = 1
        elif min_containers_needed == len(combo):
            num_min_combos += 1

    return num_min_combos

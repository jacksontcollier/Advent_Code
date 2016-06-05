#!/usr/bin/env python3

from day17 import read_container_file
from day17 import count_valid_combinations
from day17 import count_min_container_combo

PART_ONE_EGGNOG_AMOUNT = 150;

container_sizes = read_container_file('part_one_input.txt')
first_part_answer = count_valid_combinations(container_sizes, PART_ONE_EGGNOG_AMOUNT)
print("First part answer: %d" % first_part_answer)

second_part_answer = count_min_container_combo(container_sizes, PART_ONE_EGGNOG_AMOUNT)
print("Second part answer: %d" % second_part_answer)

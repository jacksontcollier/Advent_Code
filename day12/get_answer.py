#!/usr/bin/env python3

from day12 import get_file_string
from day12 import json_sum
from day12 import json_remove_red

input_data_file = "input_day12.txt"
print("Part 1 Answer: %d" % json_sum(get_file_string(input_data_file)))
red_removed = json_remove_red(get_file_string(input_data_file))
print("Part 2 Answer: %d" % json_sum(red_removed))

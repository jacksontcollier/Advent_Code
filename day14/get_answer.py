#!/usr/bin/env python3

from day14 import Reindeer
from day14 import Reindeer_Race

race = Reindeer_Race('day14_input.txt')
race.run_race(2503)
print("Part 1 answer: %d" % race.get_max_dist_traveled())

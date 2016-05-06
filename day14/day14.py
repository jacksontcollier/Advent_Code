#!/usr/bin/env python3

import re
from enum import Enum

class Reindeer_State(Enum):
    Flying = 0
    Resting = 1

class Reindeer:
    def __init__(self, name, velocity, fly_time, rest_time):
        self.name = name
        self.velocity = velocity
        self.fly_time = fly_time
        self.rest_time  = rest_time
        self.state = Reindeer_State.Resting
        self.relevant_count = 0
        self.distance_traveled = 0

    def set_state(self, new_state):
        self.relevant_count = 0
        self.state = new_state

    def advance_time(self):
        self.relevant_count += 1
        
        if self.state == Reindeer_State.Flying:
            self.distance_traveled += self.velocity
            if self.relevant_count == self.fly_time:
                self.state = Reindeer_State.Resting
                self.relevant_count = 0
        else:
            if self.relevant_count == self.rest_time:
                self.state = Reindeer_State.Flying
                self.relevant_count = 0

class Reindeer_Race:
    def __init__(self, reindeer_stats_file):
        self.reindeer = []

        with open(reindeer_stats_file) as fin:
            for line in fin.readlines():
                name = line.split()[0]
                stats = [int(s) for s in re.findall(r'\d+', line.rstrip())]
                self.reindeer.append(Reindeer(name, stats[0], stats[1], stats[2]))

    def run_race(self, race_length):
        for deer in self.reindeer:
            deer.set_state(Reindeer_State.Flying)

        for i in range(race_length):
            for deer in self.reindeer:
                deer.advance_time()

    def get_max_dist_traveled(self):
        max_dist = 0
        for deer in self.reindeer:
            max_dist = max(deer.distance_traveled, max_dist)

        return max_dist


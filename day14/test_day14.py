#!/usr/bin/env python3

import unittest

from day14 import Reindeer
from day14 import Reindeer_Race

class RunsRaceCorrectly(unittest.TestCase):
    def test_one(self):
        race = Reindeer_Race('test_001.txt')
        race.run_race(1000)
        self.assertEqual(1120, race.get_max_dist_traveled())

if __name__=='__main__':
    unittest.main()

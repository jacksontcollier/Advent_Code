#!/usr/bin/env python3

from enum import Enum

class GridConstructType(Enum):
    FROM_FILE = 1
    FROM_PREVIOUS_GRID = 2

class Animation:
    def __init__(self, initial_grid_state_file, num_steps, stuck_lights = []):
        self.num_steps = num_steps
        self.stuck_lights = stuck_lights 
        self.grid_state = Grid(initial_grid_state_file, GridConstructType.FROM_FILE)
        self.grid_state.turn_on_stuck_lights(self.stuck_lights)

    def animate(self):
        for i in range(0, self.num_steps):
            self.advance_grid_state()

    def advance_grid_state(self):
        self.grid_state = Grid(self.grid_state, GridConstructType.FROM_PREVIOUS_GRID)
        self.grid_state.turn_on_stuck_lights(self.stuck_lights)

    def count_on_lights(self):
        return self.grid_state.count_on_lights()

class Grid:
    def __init__(self, constructor_data, construction_method):
        if construction_method == GridConstructType.FROM_FILE:
            self.construct_from_file(constructor_data)
        elif construction_method == GridConstructType.FROM_PREVIOUS_GRID:
            self.construct_new_grid_state(constructor_data)
    
    def construct_from_file(self, filename):
        self.state = [] 
        with open(filename) as fin:
            for line in fin.readlines():
                row = [] 
                for light in line.rstrip():
                    row.append(light)

                self.state.append(row)

    def construct_new_grid_state(self, previous_grid):
        column_len = len(previous_grid.state)
        row_len = len(previous_grid.state[0])
        self.state = [['#' for j in range(0, row_len)] for i in range(0, column_len)]

        for i in range(0, len(previous_grid.state)):
            for j in range(0, len(previous_grid.state[i])):
                num_adjacent_on = previous_grid.count_adjacent_on(i, j)
               
                if previous_grid.light_is_on((i, j)):
                    if (num_adjacent_on == 2) or (num_adjacent_on == 3):
                        self.state[i][j] = '#'
                    else:
                        self.state[i][j] = '.'
                else:
                    if num_adjacent_on == 3:
                        self.state[i][j] = '#'
                    else:
                        self.state[i][j] = '.'
                
    def count_adjacent_on(self, i, j):
        num_on = 0
        
        adj_coords = [(i-1, j-1), (i, j-1), (i+1, j-1), (i-1, j), (i+1, j),
                      (i-1, j+1), (i, j+1), (i+1, j+1)]

        for coords in adj_coords:
            if self.light_is_on(coords):
                num_on += 1

        return num_on

    def light_is_on(self, coords):
        if (coords[0] < 0) or (coords[1] < 0):
            return False

        if coords[0] >= len(self.state):
            return False

        if coords[1] >= len(self.state[0]):
            return False
        
        return self.state[coords[0]][coords[1]] == '#'

    def count_on_lights(self):
        num_on = 0

        for row in self.state:
            for light in row:
                if light == '#':
                    num_on += 1

        return num_on

    def turn_on_stuck_lights(self, stuck_lights):
        for light_coords in stuck_lights:
            self.state[light_coords[0]][light_coords[1]] = '#'

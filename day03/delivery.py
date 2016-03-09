class GenericSanta:
    
    def __init__(self, x, y):
        self.location = (x, y) 
        
        self.directive_map = {
            '^' : (0, 1),
            '>' : (1, 0),
            'v' : (0, -1),
            '<' : (-1, 0)
        }

        self.visited_locations = { self.location : True }

    def travel_next_location(self, directive):
        if directive in self.directive_map:
            self.location = tuple(map(sum, zip(self.directive_map[directive], self.location)))
            self.visited_locations[self.location] = True

def count_houses(directions):
    santa = GenericSanta(0, 0)

    for directive in directions:
        santa.travel_next_location(directive) 

    return len(santa.visited_locations)

def robo_count(directions):
    santa = GenericSanta(0, 0)
    robo_santa = GenericSanta(0, 0)

    for index, directive in enumerate(directions):
        if (index % 2) == 0:
            santa.travel_next_location(directive)
        else:
            robo_santa.travel_next_location(directive)
    
    santa.visited_locations.update(robo_santa.visited_locations)

    return len(santa.visited_locations)

def count_floors(directions):
    return directions.count('(') - directions.count(')')

def get_position(directions):

    floor  = 0
    position = 0

    for character in directions:
        if character is '(':
            floor += 1
        elif character is ')':
            floor -= 1
        
        if (floor is -1):
            return position + 1

        position += 1

    return 0

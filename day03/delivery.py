def count_houses(directions):
    x = 0
    y = 0

    houses = []
    
    houses.append((x, y))

    for direction in directions:
        if direction is '^':
            y += 1
        elif direction is '>':
            x += 1
        elif direction is '<':
            x -= 1
        elif direction is 'v':
            y -= 1

        if (x, y) not in houses:
            houses.append((x, y))

    return len(houses)

def robo_count(directions):
    santa_x = 0
    santa_y = 0
    robo_x = 0
    robo_y = 0

    houses = []

    houses.append((santa_x, santa_y))
    
    count = 0

    for direction in directions:
        if (count % 2) is 0:
            if direction is '^':
                santa_y += 1
            elif direction is '>':
                santa_x += 1
            elif direction is '<':
                santa_x -= 1
            elif direction is 'v':
                santa_y -= 1

            if (santa_x, santa_y) not in houses:
                houses.append((santa_x, santa_y))
        else:
            if direction is '^':
                robo_y += 1
            elif direction is '>':
                robo_x += 1
            elif direction is '<':
                robo_x -= 1
            elif direction is 'v':
                robo_y -= 1

            if (robo_x, robo_y) not in houses:
                houses.append((robo_x, robo_y))
        
        count += 1

    return len(houses)

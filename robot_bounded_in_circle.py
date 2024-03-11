def is_robot_bounded(instructions):
    robot_position = {'X': 0, 'Y': 0}
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    aux = 0
    for instruction in instructions:
        current_direction = aux % len(directions)
        if instruction == 'G':
            dx, dy = directions[current_direction]
            robot_position['X'] += dx
            robot_position['Y'] += dy
        elif instruction == 'L':
            aux -= 1
        elif instruction == 'R':
            aux += 1

    current_direction = aux % len(directions)
    if (robot_position['X'] == 0 and robot_position['Y'] == 0) or current_direction != 0:
        return True
    else:
        return False


instruct = "GGLLGG"
print(is_robot_bounded(instruct))

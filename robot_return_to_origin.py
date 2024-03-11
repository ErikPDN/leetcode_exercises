def robot_return_origin(moves):
    robot_position = {'X': 0, 'Y': 0}

    for move in moves:
        if move == 'R':
            robot_position['Y'] += 1
        elif move == 'L':
            robot_position['Y'] -= 1
        elif move == 'U':
            robot_position['X'] += 1
        else:
            robot_position['X'] -= 1

    if robot_position['X'] == 0 and robot_position['Y'] == 0:
        return True
    else:
        return False


movess = "LL"
print(robot_return_origin(movess))


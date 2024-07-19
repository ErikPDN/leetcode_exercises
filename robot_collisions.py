def survivedRobotHealths(positions, healths, directions):
    sorted_positions = sorted(positions)

    p1_to_direction, p2_to_direction = 0, 1
    p1_to_health, p2_to_health = 0, 1
    while p2_to_direction < len(directions):
        if directions[p1_to_direction] == 'R' and directions[p2_to_direction] == 'L':
            if healths[p1_to_health] > healths[p2_to_health]:
                healths[p1_to_health] -= 1
                healths.pop(p2_to_health)
            elif healths[p1_to_health] < healths[p2_to_health]:
                healths[p2_to_health] -= 1
                healths.pop(p1_to_health)
            else:
                healths.pop(p2_to_health)
                healths.pop(p1_to_health)

        elif positions[p1_to_direction] > positions[p2_to_direction]:
            if directions[p1_to_direction] == 'L' and directions[p2_to_direction] == 'R':
                if healths[p1_to_health] > healths[p2_to_health]:
                    healths[p1_to_health] -= 1
                    healths.pop(p2_to_health)
                elif healths[p1_to_health] < healths[p2_to_health]:
                    healths[p2_to_health] -= 1
                    healths.pop(p1_to_health)
                else:
                    healths.pop(p2_to_health)
                    healths.pop(p1_to_health)

        else:
            p2_to_health += 2 if directions[p2_to_health] else 1
            p1_to_health = p2_to_health - 1

        p2_to_direction += 2 if directions[p2_to_direction] else 1
        p1_to_direction = p2_to_direction - 1

    return healths


pos = [37,35]
healths = [16,19]
directions = "RLRRR"
print(survivedRobotHealths(pos, healths, directions))

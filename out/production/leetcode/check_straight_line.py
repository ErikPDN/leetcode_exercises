def check_line(coordinates):
    if len(coordinates) < 2:
        return False

    x1, y1 = coordinates[0][0], coordinates[0][1]
    x2, y2 = coordinates[1][0], coordinates[1][1]

    if x2 - x1 == 0:
        x_constant = x1
        for coordinates in coordinates:
            if coordinates[0] != x_constant:
                return False
        return True

    if y2 - y1 == 0:
        y_constant = y1
        for coordinate in coordinates:
            if coordinate[1] != y_constant:
                return False

    m = (y2 - y1) / (x2 - x1)
    for coordinate in coordinates:
        curr_x = coordinate[0]
        curr_y = m * (curr_x - x1) + y1
        if curr_y != coordinate[1]:
            return False

    return True


cordinate_s = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(check_line(cordinate_s))

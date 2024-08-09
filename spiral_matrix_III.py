def spiral_matrix_III(rows, cols, rStart, cStart):
    matrix_result = []
    rCurr, cCurr = rStart, cStart

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0

    count_mov = 1
    total = rows * cols

    while len(matrix_result) < total:
        for _ in range(2):
            for _ in range(count_mov):
                if 0 <= rCurr < rows and 0 <= cCurr < cols:
                    matrix_result.append([rCurr, cCurr])

                if len(matrix_result) == total:
                    return matrix_result

                rCurr += directions[direction_index][0]
                cCurr += directions[direction_index][1]

            direction_index = (direction_index + 1) % 4

        count_mov += 1

    return matrix_result


rows = 5
cols = 6
rStart = 1
cStart = 4
print(spiral_matrix_III(rows, cols, rStart, cStart))

    
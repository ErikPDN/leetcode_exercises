def verify_won(matriz):
    for i in range(3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] != '':
            return True
        if matriz[0][i] == matriz[1][i] == matriz[2][i] != '':
            return True

    if matriz[0][0] == matriz[1][1] == matriz[2][2] != '':
        return True
    if matriz[0][2] == matriz[1][1] == matriz[2][0] != '':
        return True

    return False


def find_winner(moves):
    grid = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]

    players = ['A', 'B']
    current_player = 0

    for x, y in moves:
        grid[x][y] = players[current_player]
        if verify_won(grid):
            return players[current_player]

        current_player = (current_player + 1) % 2

    for i in range(3):
        if grid[i][0] == '' or grid[i][1] == '' or grid[i][2] == '':
            return 'Pending'
        if grid[0][i] == grid[1][i] == grid[2][i] == '':
            return 'Pending'

    return 'Draw'


move_s = [[0,0],[2,0],[1,1],[2,1],[2,2]]
print(find_winner(move_s))


# class Solution:
#     def tictactoe(self, moves: List[List[int]]) -> str:
#         # 3 x 3 grid
#         n = 3
#         empty_square = (n * n) - len(moves)
#         # rows and columns
#         rows, cols = [0] * n, [0] * n
#         # diagonals
#         primary_diagonal = 0
#         secondary_diagonal = 0
#
#         for i in range(len(moves)):
#             x, y = moves[i]
#
#             # player A
#             if i % 2 == 0:
#                 mark = 1
#             else:  # player B
#                 mark = -1
#             rows[x] += mark
#             cols[y] += mark
#
#             if x == y:
#                 primary_diagonal += mark
#             if x + y == n - 1:
#                 secondary_diagonal += mark
#
#             # check if there is same mark in a row
#             if abs(rows[x]) == n or abs(cols[y]) == n or abs(primary_diagonal) == n or abs(secondary_diagonal) == n:
#                 if mark == 1:
#                     return 'A'
#                 else:
#                     return 'B'
#
#         if empty_square == 0:
#             return 'Draw'
#
#         return 'Pending'
def diagonal_sum(mat):
    if len(mat) == 0:
        return 0
    elif len(mat) == 1:
        return mat[0][0]
    else:
        first_diagonal = []
        second_diagonal = []
        j = len(mat)
        for i in range(len(mat)):
            first_diagonal.append(mat[i][i])
            second_diagonal.append(mat[i][j-i-1])

        sum_first_diagonal = sum(first_diagonal)
        sum_second_diagonal = sum(second_diagonal)

        if len(mat) % 2 == 1:
            mid = len(mat) // 2
            sum_total = (sum_first_diagonal + sum_second_diagonal) - mat[mid][mid]

            return sum_total
        else:
            return sum_first_diagonal + sum_second_diagonal


matrix = [[4,6,7],
          [2,9,4],
          [5,5,5]]
print(diagonal_sum(matrix))

# better solution
# n = len(mat)
#         ans = 0
#
#         for i in range(n):
#             ans += mat[i][i]
#             ans += mat[n - 1 - i][i]
#         if n % 2 != 0:
#             ans -= mat[n // 2][n // 2]
#
#         return ans

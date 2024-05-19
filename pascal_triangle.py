def generate(num_rows):
    new_matrix = [[1] * (i + 1) for i in range(num_rows)]

    for row in range(num_rows):
        for col in range(row):
            if row + 1 < num_rows and col + 1 < len(new_matrix[row + 1]):
                sum_nums = new_matrix[row][col] + new_matrix[row][col+1]
                new_matrix[row+1][col+1] = sum_nums

    return new_matrix


num_linhas = 5
print(generate(num_linhas))


# best solution

# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         triangle = []
#         for i in range(numRows):
#             row = [1]
#             if i > 0:
#                 prev_row = triangle[i - 1]
#                 for j in range(1, i):
#                     row.append(prev_row[j - 1] + prev_row[j])
#                 row.append(1)
#             triangle.append(row)
#         return triangle


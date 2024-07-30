def luckyNumbers(matrix):
    lucky_numebers = []
    
    rows_len = len(matrix)
    col_len = len(matrix[0])

    for i in range(rows_len):
        smallest_n_of_row = min(matrix[i])
        for j in range(col_len):
            curr = matrix[i][j]
            if curr == smallest_n_of_row:
                col = [row[j] for row in matrix]
                biggest_n_of_col = max(col)
                if biggest_n_of_col == curr:
                    lucky_numebers.append(curr)

                break

    return lucky_numebers


matrix = [
    [1, 6, 3],
    [4, 7, 2],
    [5, 8, 9]
]
print(luckyNumbers(matrix))

# BEST SOLUTION
# def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
#         R = len(matrix)
#         C = len(matrix[0])
#         numIdxMap = {}
#         result = []

#         for i in range(R):
#             row = matrix[i]
#             minColIdx = row.index(min(matrix[i]))
#             minValInRow = matrix[i][minColIdx]
#             isLuckyNum = True
            
#             for r in range(R):
#                 if r != i and matrix[r][minColIdx] > minValInRow:
#                     isLuckyNum = False
#                     break

#             if isLuckyNum:
#                 result.append(minValInRow)

#         return result
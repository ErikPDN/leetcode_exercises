def getRow(rowIndex):
    triangle = []
    for i in range(33):
        row = [1]
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        triangle.append(row)
    
    return triangle[rowIndex]


rowIndex = 1
print(getRow(rowIndex))

# best solution

# from math import factorial as f
# def getRow(n: int):
#     output = []
#     for k in range(n+1):
#         output.append(int(f(n) / (f(k) * f(n-k))))
#     return output
#
# # Exemplo de uso
# rowIndex = 1
# print(getRow(rowIndex))  # Saída: [1, 1]

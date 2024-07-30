def reverseParentheses(s):
    list_s = list(s)
    count_parentheses = s.count('(')

    i, j = 1, 0
    while 0 < count_parentheses:
        if list_s[i] == '(':
            j = i
            i += 1

        elif list_s[i] == ')':
            k = len(list_s[j:i]) // 2
            aux_j = j
            aux_i = i
            moves = 0
            while moves < k:
                list_s[aux_j+1], list_s[aux_i-1] = list_s[aux_i-1], list_s[aux_j+1]
                aux_j += 1
                aux_i -= 1
                moves += 1

            list_s.pop(j)
            list_s.pop(i-1)
            i = 1
            j = 0
            count_parentheses -= 1

        else:
            i += 1

    return ''.join(list_s)


s = "(u(love)i)"
print(reverseParentheses(s))

# BEST SOLUTION
# def reverseParentheses(self, s: str) -> str:
#     stack = []
#
#     currString = ""
#
#     for i in range(len(s)):
#         if s[i] == '(':
#             stack.append(currString)
#             currString = ""
#         elif s[i].isalpha():
#             currString += s[i]
#         elif s[i] == ')':
#             currString = currString[::-1]
#             stackTop = stack.pop()
#             currString = stackTop + currString
#
#     return currString

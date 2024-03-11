from dados import calcular_tempo


@calcular_tempo
def valid_parentheses(s):
    check = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    stack = []

    for c in s:
        if stack and stack[-1] in check and check[stack[-1]] == c:
            stack.pop()
        else:
            stack.append(c)

    return not stack


s = '()[]{}'
resultado = valid_parentheses(s)
print(resultado)

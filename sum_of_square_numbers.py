import math

def judgeSquareSum(c):
    root = math.sqrt(c)
    if root.is_integer():
        return True

    a = 0
    b = int(math.sqrt(c))

    while a <= b:
        soma = a * a + b * b
        if soma == c:
            return True
        elif soma < c:
            a += 1
        else:
            b -= 1

    return False


x = 32
print(judgeSquareSum(x))
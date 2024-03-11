def power(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(x, -n)
    else:
        if n % 2:
            return x * power(x, n - 1)
        else:
            y = power(x, n // 2)
            return y * y


y = 0.00001
z = 2147483647
print(power(y, z))


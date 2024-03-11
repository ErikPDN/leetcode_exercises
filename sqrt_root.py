def my_sqrt(x):
    if x == 0 or x == 1:
        return x
    guess = x // 2
    while guess**2 > x:
        guess = (guess + x // guess) // 2
    return guess


n = 100
print(my_sqrt(n))

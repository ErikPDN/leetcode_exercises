def is_palimdrome(num):
    invert = 0
    original = num

    while num > 0:
        digite = num % 10
        invert = invert * 10 + digite
        num //= 10

    if invert == original:
        return True
    else:
        return False


print(is_palimdrome(12231))



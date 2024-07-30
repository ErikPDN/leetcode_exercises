def climb(n):
    if n == 0 or n == 1:
        return 1
    else:
        n_i = 1  # n0
        n_j = 1  # n1
        count = 0

        i = 1
        while i < n:
            count = n_i + n_j
            temp = n_j
            n_j += n_i
            n_i, i = temp, i+1

        return count


print(climb(n=44))


# alternative method


def climb_stairs(n):
    if n < 3:
        return n
    else:
        a, b, c = 1, 1, 0
        while n > 1:
            c = a+b
            a = b
            b = c
            n -= 1

        return c


print(climb_stairs(n=4))

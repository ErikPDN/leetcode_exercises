from functools import reduce


def array_sign(nums):
    product = reduce(lambda x, y: x * y, nums)

    if product > 0:
        return 1
    elif product < 0:
        return -1
    else:
        return 0


numbers = [-1,1,-1,1,-1]
print(array_sign(numbers))

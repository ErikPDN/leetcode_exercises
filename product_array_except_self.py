from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    left, right, product = [0] * n, [0] * n, [0] * n

    left[0] = 1
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]

    right[n - 1] = 1
    for i in reversed(range(n - 1)):
        right[i] = right[i + 1] * nums[i + 1]

    for i in range(n):
        product[i] = left[i] * right[i]

    return product


numbers = [1, 2, 3, 4]
print(product_except_self(numbers))

def singleNumber(nums):
    a = set()
    for num in nums:
        if num in a:
            a.remove(num)
        else:
            a.add(num)
    return list(a)


def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

numbers = [1, 2, 1, 3, 2, 5]
print(singleNumber(numbers))
print(single_number(numbers))
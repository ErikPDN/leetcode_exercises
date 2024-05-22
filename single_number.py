def singleNumber(nums) -> int:
    dictionary = {}
    for num in nums:
        if num in dictionary:
            dictionary[num] += 1
        else:
            dictionary[num] = 1

    return [value for value, count in dictionary.items() if count == 1][0]


numbers = [1]
print(singleNumber(numbers))

# best solution
# def singleNumber(nums) -> int:
#     return [i for i in nums if nums.count(i) == 1][0]

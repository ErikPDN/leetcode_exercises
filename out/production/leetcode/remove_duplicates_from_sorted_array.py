def remove_duplicate(nums):
    dictionary = {}

    i = 0
    while len(nums) - 1 >= i:
        if nums[i] not in dictionary:
            dictionary[nums[i]] = 1
            i += 1
        else:
            nums.pop(i)

    return len(nums)


nums = [1, 1, 2, 2, 2, 3, 4, 4]
print(remove_duplicate(nums))

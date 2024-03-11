def remove_element(nums, val):
    i = 0
    while len(nums) - 1 >= i:
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1

    return len(nums)


numbers = [3, 2, 2, 3]
target = 3

print(remove_element(numbers, target))

def remove_duplicate(nums):

    i = 0
    while len(nums) - 1 > i:
        if nums[i] == nums[i+1]:
            nums.pop(i)
        else:
            i += 1

    return nums


nums = [1, 1, 2, 2, 2, 3, 4, 4]
print(remove_duplicate(nums))

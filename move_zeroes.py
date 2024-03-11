def move_zero(nums):
    i = 0
    count_zeros = nums.count(0)

    while i < len(nums) - count_zeros:
        if nums[i] == 0:
            nums.append(nums.pop(i))
        else:
            i += 1

nums = [0,0,1]
print(move_zero(nums))

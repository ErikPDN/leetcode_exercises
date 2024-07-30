def specialArray(nums):
    for i in range(1000):
        greater_or_equal = 0
        for j in range(len(nums)):
            if nums[j] >= i:
                greater_or_equal += 1

        if greater_or_equal == i:
            return i
    
    return -1


input = [0,4,3,0,4]
print(specialArray(input))

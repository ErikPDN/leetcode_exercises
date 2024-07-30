def minDifference(nums):
    if len(nums) < 3:
        return 0

    nums.sort()

    arr1 = nums[-1] - nums[3]
    arr2 = nums[-2] - nums[2]
    arr3 = nums[-3] - nums[1]
    arr4 = nums[-4] - nums[0]

    return min(arr1, arr2, arr3, arr4)


numbers = [20,66,68,57,45,18,42,34,37,58]
print(minDifference(numbers))

def is_monotonic(nums):
    ant = nums[0]
    if nums[0] < nums[-1]:
        for i in range(1, len(nums)):
            if nums[i] < ant:
                return False

            ant = nums[i]

        return True
    elif nums[0] >= nums[-1]:
        for i in range(1, len(nums)):
            if nums[i] > ant:
                return False

            ant = nums[i]

        return True


n = [1,3,2]
print(is_monotonic(n))
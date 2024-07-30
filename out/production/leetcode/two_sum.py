def two_sum(nums, target):
    visited = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in visited:
            return [visited[complement], i]
        visited[num] = i
    return []


nums = [2, 11, 10, 9, 15, 7]
the_target = 9
print(two_sum(nums, the_target))



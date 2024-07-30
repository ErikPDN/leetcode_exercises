def remove_element(nums, val):
    n = nums.count(val)
    for _ in range(n):
        nums.remove(val)
    return len(nums)


numbers = [3, 2, 2, 3]
target = 3

print(remove_element(numbers, target))

# best solution

# n = nums.count(val)
# k = 0
# for _ in range(n):
#     nums.remove(val)
# return len(nums)


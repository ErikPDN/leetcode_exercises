from collections import Counter


def minIncrementForUnique(nums):
    nums.sort()
    moves = 0

    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            increment = nums[i - 1] - nums[i] + 1
            nums[i] += increment
            moves += increment

    return moves


numbers = [3, 2, 1, 2, 1, 7]
print(minIncrementForUnique(numbers))


# def minIncrementForUnique2(nums):
#     moves = 0
#     count = Counter(nums)
#     used = set(nums)
#
#     for num in nums:
#         while count[num] > 1:
#             count[num] -= 1
#             new_num = num + 1
#             while new_num in used:
#                 new_num += 1
#                 moves += 1
#             count[new_num] = 1
#             used.add(new_num)
#             moves += 1
#
#     return moves
#
#
# numbers = [3, 2, 1, 2, 1, 7]
# print(minIncrementForUnique2(numbers))

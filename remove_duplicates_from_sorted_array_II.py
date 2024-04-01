def remove_duplicates(nums):
    dictionary = {}

    k = 0
    while len(nums) - 1 >= k:
        if nums[k] not in dictionary:
            dictionary[nums[k]] = 1
            k += 1
        else:
            dictionary[nums[k]] += 1
            if dictionary[nums[k]] > 2:
                nums.pop(k)
                continue
            k += 1

    return k


numbers = [1,1,1,2,2,3]
print(remove_duplicates(numbers))

# best solution
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         prev = nums[0]
#         q = 1
#         k = 1
#         while k < len(nums):
#             curr = nums[k]
#             if curr == prev:
#                 q += 1
#                 if q > 2:
#                     nums.pop(k)
#                 else:
#                     k += 1
#             else:
#                 q = 1
#                 k += 1
#             prev = curr
#         return len(nums)


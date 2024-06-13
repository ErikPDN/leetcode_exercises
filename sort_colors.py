def sortColors(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

numbers = [2,0,2,1,1,0]
print(sortColors(numbers))

# best solution
# m = dict()
#         for n in nums:
#             m[n] = m.get(n,0) + 1
#         s = 0
#         for i in (0,1,2):
#             if i in m:
#                 for j in range(s, s + m[i]):
#                     nums[j] = i
#                 s = j + 1

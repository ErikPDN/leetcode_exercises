def largest_perimeter(nums):
    if len(nums) < 3:
        return 0

    ord_nums = sorted(nums)
    while len(ord_nums) >= 3:
        a = ord_nums[-1]
        b = ord_nums[-2]
        c = ord_nums[-3]

        if a + b > c and b + c > a and c + a > b:
            return a + b + c

        ord_nums.pop()

    return 0


numbers = [1,2,1,10]
print(largest_perimeter(numbers))


# best solution

# class Solution:
#     def largestPerimeter(self, nums: List[int]) -> int:
#         nums=sorted(nums,reverse=True)
#         #@print(nums)
#         for i in range(0,len(nums)-2,1):
#             if nums[i+1]+nums[i+2]>nums[i]:
#                 #print("P")
#                 return nums[i]+nums[i+1]+nums[i+2]
#         return 0


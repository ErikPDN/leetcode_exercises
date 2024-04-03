def rotate(nums, k):
    while k > 0:
        nums.insert(0, nums[-1])
        nums.pop()
        k -= 1


numbers = [1,2,3,4,5,6,7]
k = 3
print(rotate(numbers, k))
print(numbers)

# other way

# def rotate(self, nums: List[int], k: int) -> None:
#     l = k % len(nums)
#     nums[0:len(nums)] = nums[-l:] + nums[:-l]

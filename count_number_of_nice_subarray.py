def numberOfSubarray(nums, k):
    n = len(nums)
    total_nice_sub_arrays = 0

    count_k = 0
    low, high = 0, 0
    prefix_count = 0

    while high < n:
        if nums[high] % 2 == 1:
            count_k += 1
            prefix_count = 0

        while count_k == k:
            if nums[low] % 2 == 1:
                count_k -= 1

            low += 1
            prefix_count += 1

        total_nice_sub_arrays += prefix_count
        high += 1

    return total_nice_sub_arrays


numbers = [2,2,2,1,2,2,1,2,2,2]
x = 2
print(numberOfSubarray(numbers, x))

# for start in range(n):
#     for end in range(start, n):
#         subarray = nums[start:end + 1]
#
#         if len(subarray) >= k:
#             count_odds = 0
#             for item in subarray:
#                 if item % 2 == 1:
#                     count_odds += 1
#
#             if count_odds == k:
#                 total_nice_sub_arrays += 1
#                 sub_arrays.append(subarray)
#
# return sub_arrays
def subarray_sums_divisible_by_k(arr, k):
    prefix_sum = {0: 1}
    current_sum = 0
    count = 0

    for num in arr:
        current_sum += num
        remainder = current_sum % k

        if remainder < 0:
            remainder += 1

        if remainder in prefix_sum:
            count += prefix_sum[remainder]

        if remainder in prefix_sum:
            prefix_sum[remainder] += 1
        else:
            prefix_sum[remainder] = 1

    return count


nums = [4, 5, 0, -2, -3, 1]
k = 5
print(subarray_sums_divisible_by_k(nums, k))


def containsNearbyDuplicates(nums, k):
    index_map = {}

    for i, num in enumerate(nums):
        if num in index_map:
            if i - index_map[num] <= k:
                return True

        index_map[num] = i

    return False


arr = [1, 2, 3, 1]
print(containsNearbyDuplicates(arr, 2))

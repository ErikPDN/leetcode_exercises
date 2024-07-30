def merge(nums1, m, nums2, n):
    i, j = m - 1, n - 1
    k = m + n - 1

    while k >= 0 and j >= 0 and i >= 0:
        if nums2[j] >= nums1[i]:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1

    # When loop terminates but still some values from second array is not copied
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


numbers_1 = [2,0]
m = 1
numbers_2 = [1]
n = 1
merge(numbers_1, m, numbers_2, n)
print(numbers_1)

# def insertion_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     for j in range(1, len(arr)):
#         key = arr[j]
#         i = j - 1
#         while i >= 0 and arr[i] > key:
#             arr[i+1] = arr[i]
#             i = i - 1
#         arr[i+1] = key
#
#     return arr




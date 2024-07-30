def relativeSortArray(arr1, arr2):
    relative_sort = []
    
    for i in range(len(arr2)):
        j = 0
        while j < len(arr1):
            if arr2[i] == arr1[j]:
                relative_sort.append(arr1[j])
                arr1.pop(j)
                continue
            j += 1

    relative_sort += (sorted(arr1))

    return relative_sort


nums1 = [2,3,1,3,2,4,6,7,9,2,19]
nums2 = [2,1,4,3,9,6]
print(relativeSortArray(nums1, nums2))


# best solution
#
# hash_map = {}
# for i in range(len(arr2)):
#     hash_map[arr2[i]] = i
#
# for i in range(len(arr1)):
#     if arr1[i] not in hash_map:
#         hash_map[arr1[i]] = 1000 + arr1[i]
# arr1.sort(key=lambda x: hash_map[x])
# return arr1

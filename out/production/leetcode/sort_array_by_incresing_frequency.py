from collections import Counter


def frequencySort(nums):
    freq = Counter(nums)
    nums.sort(key=lambda x: (freq[x], -x))

    return nums


numbers = [2,3,1,3,2]
print(frequencySort(numbers))
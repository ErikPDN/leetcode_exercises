def countTiplets(arr):
    arr.insert(0, 0)
    n = len(arr)
    for i in range(n - 1):
        arr[i+1] ^= arr[i]
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                res += j - i + 1

    return res


arr = [2,3,1,6,7]
print(countTiplets(arr))
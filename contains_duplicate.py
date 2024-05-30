def containsDuplicate(nums):
    a = set()
    for num in nums:
        if num not in a:
            a.add(num)
        else:
            return True
    
    return False


arr = [1,2,3,1]
print(containsDuplicate(arr))

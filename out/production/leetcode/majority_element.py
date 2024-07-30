def majority_element(nums):
    count = 0
    candidate = 0

    for num in nums:
        if count == 0:
            candidate = num

        if candidate == num:
            count += 1
        else:
            count -= 1
    return candidate


numbers = [2,2,1,1,1,2,2]
print(majority_element(numbers))

def numTeams(rating):
    if len(rating) < 3:
        return 0

    _set = set()

    n = len(rating)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                    _set.add((rating[i], rating[j], rating[k]))

    return len(_set)


rat = [1,2,3, 4]
print(numTeams(rat))

# elif rating[i] > rating[j] > rating[k]:
#     nums = [rating[i], rating[j], rating[k]]
#     set.add(nums)
#     j += 1
#     k += 1

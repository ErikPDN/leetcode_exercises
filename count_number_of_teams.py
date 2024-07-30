def numTeams(rating):
    n = len(rating)
    count = 0

    for j in range(n):
        left_less, left_more = 0, 0
        right_less, right_more = 0, 0

        for i in range(j):
            if rating[i] < rating[j]:
                left_less += 1
            if rating[i] > rating[j]:
                left_more += 1

        for k in range(j + 1, n):
            if rating[k] < rating[j]:
                right_less += 1
            if rating[k] > rating[j]:
                right_more += 1

        count += left_less * right_more + left_more * right_less

    return count


rat = [1,2,3,4]
print(numTeams(rat))

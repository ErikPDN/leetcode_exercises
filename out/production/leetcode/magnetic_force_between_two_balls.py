def maxDistance(position, m):
    position.sort()
    low, upper = 0,  position[-1] - position[0]

    while low <= upper:
        mid = (low + upper) // 2
        total = 1
        last_position = position[0]

        for i in range(1, len(position)):
            if position[i] - last_position >= mid:
                total += 1
                last_position = position[i]

        if total >= m:
            low = mid + 1

        else:
            upper = mid - 1

    return low - 1


pos = [5,4,3,2,1,1000000000]
x = 2
print(maxDistance(pos, x))

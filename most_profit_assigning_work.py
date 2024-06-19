def maxProfitAssignment(difficulty, profit, worker):
    dictionary = {}

    for i in range(len(difficulty)):
        dictionary[difficulty[i]] = max(profit[i], dictionary.get(difficulty[i], 0))

    sort_difficulty = sorted(dictionary.keys())
    sort_profit = [dictionary[d] for d in sort_difficulty]

    max_profit_at_difficulty = [0] * len(sort_difficulty)
    curr_max = 0
    for i in range(len(sort_difficulty)):
        curr_max = max(curr_max, sort_profit[i])
        max_profit_at_difficulty[i] = curr_max

    def binarySearch(target):
        low, high = 0, len(sort_difficulty) - 1
        while low <= high:
            mid = (low + high) // 2
            if sort_difficulty[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1

        return max_profit_at_difficulty[high] if high >= 0 else 0

    total_profit = sum(binarySearch(w) for w in worker)
    return total_profit


difficulty = [5,50,92,21,24,70,17,63,30,53]
profit = [68,100,3,99,56,43,26,93,55,25]
worker = [96,3,55,30,11,58,68,36,26,1]
print(maxProfitAssignment(difficulty, profit, worker))
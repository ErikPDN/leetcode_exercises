def threeConsecutiveOdds(arr):
    verify_odds = 0

    for num in arr:
        if num % 2 == 1:
            verify_odds += 1
            if verify_odds == 3:
                return True
        else:
            verify_odds = 0

    return False


odds = [1, 1, 1]
print(threeConsecutiveOdds(odds))

def count_odds(low, high):
    if low % 2 == 0:
        low += 1

    if high % 2 == 0:
        high -= 1

    count = (high - low) // 2 + 1

    return count


baixo, alto = 3,  7
print(count_odds(baixo, alto))


def max_profit(prices):
    if not prices or len(prices) < 2:
        return 0

    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


precos = [1,2,3,4,5]
print(max_profit(precos))

def max_profit(prices):
    min_price, max_profit = float('inf'), 0
    for p in prices:
        if p < min_price:
            min_price = p
        elif p - min_price > max_profit:
            max_profit = p - min_price
    return max_profit


preco = [7,1,5,3,6,4]
print(max_profit(preco))

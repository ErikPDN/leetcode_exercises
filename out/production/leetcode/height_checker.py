def heightChecker(heights):
    count = 0
    order_heights = sorted(heights)
    for i in range(len(heights)):
        if heights[i] != order_heights[i]:
            count += 1
    
    return count


alturas = [1,1,4,2,1,3]
print(heightChecker(alturas))

# best time solution
# def heightChecker(heights):
#     return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))

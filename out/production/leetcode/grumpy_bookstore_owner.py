def maxSatisfied(customers, grumpy, minutes):
    satisfied = 0
    i = 0
    while i + 1 <= len(customers):
        if grumpy[i] == 0:
            satisfied += customers[i]
            customers[i] = 0

        i += 1

    max_satisfied = 0
    for j in range(0, len(customers)):
        if sum(customers[j:j+minutes]) > max_satisfied:
            max_satisfied = sum(customers[j:j+minutes])

    return max_satisfied + satisfied


customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutos = 3
print(maxSatisfied(customers, grumpy, minutos))
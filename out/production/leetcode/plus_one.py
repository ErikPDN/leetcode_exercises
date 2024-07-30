def plus_one(lst):
    i, j = 0, (len(lst) - 1)
    numbers = 0
    while j >= 0:
        numbers += lst[i] * 10**j
        i += 1
        j -= 1

    numbers += 1

    str_number = str(numbers)
    list_numbers = [int(digit) for digit in str_number]

    return list_numbers


nums = [9]
print(plus_one(nums))

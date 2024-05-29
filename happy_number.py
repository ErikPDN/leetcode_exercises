def isHappy(n: int) -> bool:
    str_num = str(n)
    dictionary = {}

    while n > 0:
        sum_num = 0
        for num in str_num:
            sum_num += pow(int(num), 2)
            
        if sum_num == 1:
            return True
        
        if sum_num in dictionary:
            return False

        dictionary[sum_num] = 1
        n = sum_num
        str_num = str(sum_num)

    return False

# best solution
# def is_happy(n: int) -> bool:
#     a = set()
#     while n != 1 and n not in a:
#         a.add(n)
#         n = sum(int(digit) ** 2 for digit in str(n))
#     return n == 1


num = 2
print(isHappy(num))

def add_bin(a, b):
    a_int = bin_correspondente(a)
    b_int = bin_correspondente(b)
    sum_a_b = a_int + b_int
    res = bin(sum_a_b)[2:]

    return res


def bin_correspondente(bin_nums):
    i, j = 0, len(bin_nums) - 1
    dec_num = 0
    while i < len(bin_nums):
        dec_num += bin_nums[j] * 2**i
        i += 1
        j -= 1
    return dec_num


a = '1010'
list_a = [int(digit) for digit in a]
b = '1011'
list_b = [int(digit) for digit in b]
print(add_bin(list_a, list_b))


# best solution
#
# def addBinary(self, a: str, b: str) -> str:
#     n1 = int(a, 2)
#     n2 = int(b, 2)
#
#     return bin(n1 + n2)[2:]






def findComplement(num: int) -> int:
    number_to_bin_str = bin(num)
    list_complement = [number_to_bin_str[:2]]

    for i in range(2, len(number_to_bin_str)):
        if number_to_bin_str[i] == '0':
            list_complement.append('1')
        else:
            list_complement.append('0')

    binary_number = ''.join(list_complement)

    return int(binary_number, 2)


number = 5
print(findComplement(number))

# best solution
# def findComplement(self, num: int) -> int:
#     mask = num
#     mask |= mask >> 1
#     mask |= mask >> 2
#     mask |= mask >> 4
#     mask |= mask >> 8
#     mask |= mask >> 16
#
#     return num ^ mask

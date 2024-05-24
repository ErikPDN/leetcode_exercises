def reverse_bits(n):
    bin_str = bin(n)[2:].zfill(32)
    reversed_bin_str = bin_str[::-1]

    return int(reversed_bin_str, 2)


n = 0b0000010100101000001111010011100
print(reverse_bits(n))

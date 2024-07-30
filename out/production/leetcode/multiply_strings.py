def convert_int(string):
    num_total = 0
    j = 0
    for i in range(len(string) - 1, -1, -1):
        num = 0
        while True:
            if string[i] == str(num):
                break

            num += 1

        num_total += num * 10**j
        j += 1

    return num_total


def multiply(num1, num2):
    num1_int = convert_int(num1)
    num2_int = convert_int(num2)

    return str(num1_int * num2_int)


num_1 = "123456789"
num_2 = "987654321"
print(multiply(num_1, num_2))

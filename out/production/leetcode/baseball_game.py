def baseball(operations):
    actions = {'C', 'D', '+'}
    record = []
    for operation in operations:
        if operation[0] == '-' or operation.isdigit():
            record.append(int(operation))
        elif operation == 'C':
            record.pop()
        elif operation == 'D':
            record.append(record[-1] * 2)
        elif operation == '+':
            record.append(record[-1] + record[-2])

    return sum(record)


ops = ["5","-2","4","C","D","9","+","+"]
print(baseball(ops))
# fazer resolution usando dict action = { C, D, + }

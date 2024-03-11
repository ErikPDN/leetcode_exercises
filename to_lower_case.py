def to_lower_case(s):
    lower_s = []
    for l in s:
        lower_s.append(l.lower())

    return ''.join(lower_s)


s = 'SOMETHING'
print(to_lower_case(s))


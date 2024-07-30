def maximumGain(s, x, y):
    arr_highest_score = []

    if x >= y:
        highest_score = x
        lowest_score = y
        arr_highest_score.append("ab")
        arr_highest_score.append("ba")
    else:
        highest_score = y
        lowest_score = x
        arr_highest_score.append("ba")
        arr_highest_score.append("ab")

    score = 0

    p1, p2 = 0, 1
    while p2 < len(s) and s:
        if s[p1:p2+1] == arr_highest_score[0]:
            s = s[:p1] + s[p2+1:]
            score += highest_score
            p1 -= 1
            p2 -= 1
        else:
            p1 = p2
            p2 += 1

    p1, p2 = 0, 1
    while p2 < len(s) and s:
        if s[p1:p2+1] == arr_highest_score[1]:
            s = s[:p1] + s[p2+1:]
            score += lowest_score
            p1 -= 1
            p2 -= 1
        else:
            p1 = p2
            p2 += 1

    return score


s = "aabbaaxybbaabb"
x = 4
y = 5
print(maximumGain(s, x, y))

# BEST SOLUTION
# def maximumGain(self, s: str, x: int, y: int) -> int:
#     letter_a = "a"
#     if x < y:
#         letter_a = "b"
#         x, y = y, x

#     total = 0
#     dxy = x - y
#     ab_count = a_count = b_count = 0

#     for char in s:
#         if char not in "ab":
#             if b_count > a_count:
#                 a_count, b_count = b_count, a_count
#             if a_count > 0:
#                 total += ab_count * dxy + b_count * y
#                 ab_count = a_count = b_count = 0

#         elif char == letter_a:
#             a_count += 1

#         else:
#             b_count += 1
#             if a_count > ab_count:
#                 ab_count += 1

#     total += ab_count * dxy + min(a_count, b_count) * y
#     return total


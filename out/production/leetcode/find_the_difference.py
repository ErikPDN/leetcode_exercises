import random
import string


def shuffle_string(s):
    list_chars_s = list(s)
    random.shuffle(list_chars_s)
    random_char = random.choice(string.ascii_letters).lower()
    list_chars_s.append(random_char)

    return ''.join(list_chars_s)


def find_difference(s, t):
    list_s = list(s)
    list_t = list(t)
    for i in range(len(list_s)):
        for j in range(len(list_t)):
            if list_s[i] == list_t[j]:
                list_t.pop(j)
                break

    return ''.join(list_t)


s1 = 'abcd'
t = shuffle_string(s1)
print(t)
print(find_difference('abcd', 'abcde'))

# another solution

# return chr(sum(ord(c) for c in t) - sum(ord(c) for c in s))

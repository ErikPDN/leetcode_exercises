from collections import Counter


def is_anagram(s, t):
    return Counter(s) == Counter(t)


s = "abc"
t = "cba"
print(is_anagram(s, t))


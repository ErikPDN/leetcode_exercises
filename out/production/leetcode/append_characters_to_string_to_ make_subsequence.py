def appendCharacters(s, t):
    if not s or not t:
        return 0

    longest_prefix = t
    i = 0
    while i < len(longest_prefix) and s[i] == t[i]:
        i += 1

    longest_prefix = longest_prefix[:i]
    length = len(longest_prefix)

    i, j = length, length
    while i < len(s[length:]) and j < len(t):
        if s[i] == t[j]:
            j += 1
            i += 1
            continue
        i += 1

    new_s = s
    new_s += t[j:]

    return len(new_s) - len(s)


s = "abcde"
t = "a"
print(appendCharacters(s, t))


# best memory solution

# def appendCharacters(s: str, t: str) -> int:
#     it = iter(s)
#     matching_count = sum(1 for char in t if char in it)
#     return len(t) - matching_count


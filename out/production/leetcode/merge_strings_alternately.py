def merge_strings(word1, word2):
    maximum_range = max(len(word1), len(word2))
    smaller_word = word1 if len(word1) < len(word2) else word2
    bigger_word = word1 if len(word1) > len(word2) else word2
    strings = []

    for i in range(maximum_range):
        if i > len(smaller_word) - 1:
            strings.append(bigger_word[i])
        else:
            strings.append(word1[i] + word2[i])

    return ''.join(strings)


word1 = "abc"
word2 = "pqr"
print(merge_strings(word1, word2))

from collections import Counter

def longestPalindrome(s):
    count = Counter(s)

    length = 0
    odd = False

    for i in count.values():
        length += i // 2 * 2
        if i % 2 == 1:
            odd = True

    if odd:
        length += 1

    return length


string = 'abccccddc'
print(longestPalindrome(string))

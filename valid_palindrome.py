def isPalindrome(s):
    for letter in s:
        if not letter.isalpha() and not letter.isdigit():
            s = s.replace(letter, '')

    new_s = s.lower()

    return new_s[::-1] == new_s


string = "0P"
print(isPalindrome(string))


# best solution
# def is_palindrome(s):
#     s = ''.join(filter(str.isalnum, s))
#     s = s.lower()
#     return s == s[::-1]
#
#
# string = "0P"
# print(is_palindrome(string))
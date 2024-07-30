def titleToNumber(columnTitle):
    number = 0
    for letter in columnTitle:
        number = number * 26 + (ord(letter) - 64)
    return number


title = 'ZZ'
print(titleToNumber(title))
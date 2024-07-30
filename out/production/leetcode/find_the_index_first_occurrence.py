def find(string, substring):
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            return i
    return -1


string = 'iosbutsad'
substring = "sad"
print(find(string, substring))

def commonChars(words):
    final_common = []
    common = list(words[0])
    for word in words[1:]:
        final_common = []
        i = 0
        while i < len(common):
            j = 0
            while j < len(word) and common:
                if common[i] == word[j]:
                    final_common.append(word[j])
                    word = word[:j] + word[j+1:]
                    common.pop(i)
                    j = 0
                    i = 0
                    continue
                j += 1
            i += 1
        common = final_common

    return final_common


arr = ["cool","lock","cook"]
print(commonChars(arr))


# best solution

# def commonChars(self, words: List[str]) -> List[str]:
#     from collections import Counter
#     from typing import List
#
#     # Initialize a Counter object with the characters of the first word
#     common = Counter(words[0])
#
#     # Iterate over the remaining words and update the common Counter object
#     for word in words[1:]:
#         # Initialize a Counter object for the current word
#         word_count = Counter(word)
#         # Update the common Counter object to only include characters present in both
#         common &= word_count
#
#     # Convert the common Counter object to a list of characters
#     result = []
#     for char, count in common.items():
#         result += [char] * count
#
#     return result
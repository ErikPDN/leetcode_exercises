def longest_common_prefix(strs):
    if not strs:
        return ""

    common_prefix = strs[0]

    for word in strs[1:]:
        i = 0
        while i < len(common_prefix) and i < len(word) and common_prefix[i] == word[i]:
            i += 1

        common_prefix = common_prefix[:i]

    return common_prefix


strs = ['flower', 'flow', 'flight']
print(longest_common_prefix(strs))

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    dic = {}
    for i in range(len(s)):
        if s[i] in dic:
            if dic[s[i]] != t[i]:
                return False
        else:
            if t[i] in dic.values():
                return False
            dic[s[i]] = t[i]
    return True


a = "badc"
b = "baba"
print(isIsomorphic(a, b))

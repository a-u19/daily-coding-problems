"""
Created by Uthayathasan Arjun SF1-UK-F-4 (q659406)
Created on 11/06/2025 at 10:50
"""
def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
    d = {}
    res = [l for l in baseStr]
    for i in range(len(s1)):
        min_letter = min(s1[i], s2[i])
        other_letter = max(s1[i], s2[i])
        d[other_letter] = min_letter
    print(d)

    for key,value in d.items():
        while True:
            if value in d.keys() and d[key] > d[value]:
                d[key] = d[value]
            else:
                break

    for i in range(len(res)-1):
        res[i] = d[res[i]]

    return "".join(res)

# print(smallestEquivalentString("abc", "cde", "eed"))
print(smallestEquivalentString("leetcode", "programs", "sourcecode"))
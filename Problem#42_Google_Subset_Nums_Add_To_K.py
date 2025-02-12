"""
This problem was asked by Google.
Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.
Integers can appear more than once in the list. You may assume all numbers in the list are positive.
For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""
s =  [12, 1, 61, 5, 9, 2]
k = 24
res = []

def find_subset(s:list, k:int) -> list:
    def backtrack(start_i:int, current_sum:int, current_subset:list):
        if current_sum == k:
            return current_subset
        elif current_sum > k:
            return None
        for i in range(start_i, len(s)):
            res = backtrack(i+1, current_sum + s[i], current_subset + [s[i]])
            if res is not None:
                return res
        return None

    return backtrack(0, 0, [])

res = find_subset(s, k)
print(res)
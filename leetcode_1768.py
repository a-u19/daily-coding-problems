"""
leetcode_1768.py Created by Uthayathasan Arjun SF1-UK-F-4 (q659406)
Created on 12/05/2026 at 15:05
"""
class Solution:
	def mergeAlternately(self, word1: str, word2: str) -> str:
		return "".join(
			[a + b for a, b in zip(word1, word2)]
			+ ([word2[len(word1):]] if len(word2) > len(word1) else [word1[len(word2):]])
		)


s = Solution()
print(s.mergeAlternately("abc", "pqr"))
print(s.mergeAlternately("ab", "pqrs"))
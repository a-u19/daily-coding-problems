"""
leetcode_1431.py Created by Uthayathasan Arjun SF1-UK-F-4 (q659406)
Created on 20/05/2026 at 14:41
"""
from typing import List


class Solution:
	def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
		max_candies = max(candies)
		return [c + extraCandies >= max_candies for c in candies]
	
s = Solution()
print(s.kidsWithCandies([2,3,5,1,3], 3))
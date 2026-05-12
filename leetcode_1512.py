class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        s = "".join(str(n) for n in nums)
        print(s)
        

Solution().numIdenticalPairs([1,2,3,1,1,3])
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        total = 0
        j = 0
        while j < len(prices) - 1:
            curr_min  = curr_max = prices[j]
            i = j  + 1
            while i < len(prices) and prices[i] > curr_max:
                curr_max = prices[i]
                i += 1
            total += curr_max - curr_min
            i += 1
            j = i - 1
        return total

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([1,2,3,4,5]))
print(s.maxProfit([7,6,4,3,1]))
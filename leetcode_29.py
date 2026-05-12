class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        is_pos =  (dividend < 0) == (divisor < 0)
        divisor = abs(divisor)
        curr = abs(dividend)
        if divisor == 1:
            return curr if is_pos else -curr
        counter = 0
        while curr >= divisor:
            curr -= divisor
            counter += 1
        counter = counter if is_pos else -counter
        minus_limit = -(2**31)
        plus_limit = (2**31 - 1)
        return min(max(counter, minus_limit), plus_limit)

s = Solution()
inp1 = [10, 3]
inp2 = [7, -3]
inp3 = [1,1]
inp4 = [-1, -1]
inp5 = [-1, 1]
inp6 = [-2147483648, -1]
inps = [inp3, inp6]
for inp in inps:
    print(s.divide(inp[0], inp[1]))

"""
pos pos pos
pos neg neg
neg pos neg
neg neg pos
"""
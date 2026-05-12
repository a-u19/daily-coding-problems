class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        num_operation = 0

        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                temp = num1 // num2
                num1 %= num2
                num_operation += temp
            else:
                temp = num2 // num1
                num2 %= num1
                num_operation += temp
        return num_operation

s = Solution()
nums = [[2,3], [10,10]]
for num in nums:
    print(s.countOperations(num[0],num[1]))
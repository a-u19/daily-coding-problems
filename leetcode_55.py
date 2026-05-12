class Solution:
    # def canJump(self, nums: list[int]) -> bool:
    #     memo = {}
    #
    #     def can_reach(i:int):
    #         if i in memo:
    #             return memo[i]
    #         if i == len(nums) - 1:
    #             return True
    #         if nums[i] == 0:
    #             return False
    #         for j in range(1, nums[i] + 1):
    #             if i + j < len(nums) and can_reach(i + j):
    #                 memo[i] = True
    #                 return True
    #         memo[i] = False
    #         return False
    #
    #     return can_reach(0)

    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True
        return True

s = Solution()
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3, 2, 1, 0, 4]))  # False (Stuck at 0)
class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        total = nums[0]
        temp_total = nums[0]
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                if temp_total > total:
                    total = temp_total
                # print(f"temp total is {temp_total}")
                temp_total = nums[i]
            else:
                temp_total += nums[i]

        return max(total, temp_total)


s = Solution()
nums1 = [10,20,30,5,10,50]
nums2 = [10,20,30,40,50]
nums3 = [12,17,15,13,10,11,12]
nums4 = [3,6,10,1,8,9,9,8,9]
nums = [nums1,nums2,nums3,nums4]

for num in nums:
    print(s.maxAscendingSum(num))
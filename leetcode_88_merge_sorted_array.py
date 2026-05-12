class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) != 0:
            p1 = p2 = 0
            while p1 < m + n - 1 and p2 < n:
                # print(nums1[p1], nums2[p2])
                if nums1[p1] <= nums2[p2]:
                    p1 += 1
                else:
                    for p in range(n + m - 1, p1, -1):
                        nums1[p] = nums1[p - 1]
                    nums1[p1] = nums2[p2]
                    p2 += 1
            if p2 == 0:
                nums1[-n:] = nums2
            elif p2 < n:
                nums1[-(n-p2):] = nums2[p2:]
            print(nums1)

s = Solution()
s.merge([2,0], 1, [1], 1)
s.merge([1,2,3,0,0,0],3, [4,5,6],3)
s.merge([1,2,3,0,0,0],3, [2,5,6],3)
s.merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5)
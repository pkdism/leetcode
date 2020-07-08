"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = list(sorted(nums))
        n = len(nums)
        if n < 3:
            return []
        for i in range(n-2):
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    res.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        return res
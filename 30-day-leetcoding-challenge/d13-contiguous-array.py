"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1. 
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        res = 0
        
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1
        
        left = []
        cur_sum = 0
        for x in nums:
            cur_sum += x
            left.append(cur_sum)
        
        for i in range(n):
            if left[i] == 0 and i + 1 > res:
                res = i + 1
        
        h = {}
        
        for i in range(n):
            if left[i] in h:
                res = max(res, i - h[left[i]])
            else:
                h[left[i]] = i
                
        return res

"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1. 
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        max_len = 0
        start = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1
        
        left_sums = []
        cur_sum = 0
        
        for x in nums:
            cur_sum += x
            left_sums.append(cur_sum)
            
        for i in range(n):
            if left_sums[i] == 0:
                max_len = max(max_len, i + 1)
                
        h = {}
        for i in range(n):
            if left_sums[i] in h:
                max_len = max(max_len, i-h[left_sums[i]])
            else:
                h[left_sums[i]] = i
        
        return max_len
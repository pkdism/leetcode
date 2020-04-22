"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
"""


from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        all_sums = defaultdict(lambda : 0)
        ans, curr = 0, 0
        n = len(nums)
        for i in range(n):
            curr += nums[i]
            
            if curr == k:
                ans += 1
            
            if (curr - k) in all_sums:
                ans += all_sums[curr - k]
            
            all_sums[curr] += 1
        
        return ans
        

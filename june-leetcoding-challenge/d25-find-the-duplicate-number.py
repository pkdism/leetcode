"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
"""


from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for k, v in counts.items():
            if  v > 1:
                return k
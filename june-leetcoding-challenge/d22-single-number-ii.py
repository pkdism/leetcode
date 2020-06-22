"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
"""


from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for k, v in c.items():
            if v == 1:
                return k
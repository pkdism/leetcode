"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. 
Find the two elements that appear only once.
"""


from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        res = []
        for k, v in counts.items():
            if v == 1:
                res.append(k)
        return res
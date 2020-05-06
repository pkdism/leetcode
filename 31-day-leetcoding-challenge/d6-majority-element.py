"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
"""


from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        c = 1
        m = nums[0]
        for i in range(1, n):
            if nums[i] == m:
                c += 1
            elif c > 0:
                c -= 1
            else:
                c = 0
                m = nums[i]
        return m
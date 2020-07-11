"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ps = []
        for binary in range(2**n):
            temp = binary
            val = []
            pos = n-1
            while temp > 0:
                if temp%2 == 1:
                    val.append(nums[pos])
                pos -= 1
                temp //= 2
            ps.append(val)
        return ps
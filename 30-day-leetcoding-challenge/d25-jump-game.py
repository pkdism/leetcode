"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
            if len(nums) == 1:
                return True
            all_zeros = True
            max_needed = 1
            n = len(nums)
            for i in range(n-2, -1, -1):
                if nums[i] != 0:
                    all_zeros = False
                if nums[i] < max_needed:
                    max_needed += 1
                else:
                    max_needed = 1
            if all_zeros == True:
                return False
            if max_needed > 1:
                return False
            return True
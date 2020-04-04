"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""


class Solution:
    def moveZeroes(self, a: List[int]) -> None:
        n = len(a)
        slow, fast = 0, 0
        while True:
            while slow < n and a[slow] != 0:
                slow += 1
            fast = slow + 1
            while fast < n and a[fast] == 0:
                fast += 1
            if fast == n or slow == n:
                break
            a[slow] = a[fast]
            a[fast] = 0
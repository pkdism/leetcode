"""
Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.
"""


class Solution:
    def countElements(self, arr: List[int]) -> int:
        m = max(arr) + 1
        count = [0]*m
        for i in arr:
            count[i] += 1
        res = 0
        for i in range(m-1):
            if count[i+1] > 0:
                res += count[i]
        return res
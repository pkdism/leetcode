"""
Given an integer, write a function to determine if it is a power of two.
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 0:
            if n%2 != 0:
                if n == 1:
                    return True
                else:
                    return False
            n = n//2
        return False
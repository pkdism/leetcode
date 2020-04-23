"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m < n//2:
            return 0
        else:
            res = n
            for x in range(m, n):
                res = res & x
            return res
        
"""
Given a positive integer, output its complement number. 
The complement strategy is to flip the bits of its binary representation.
"""


class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        k = 0
        while num > 0:
            res += ((1 - num%2)*(2**k))
            k += 1
            num = num//2
        return res
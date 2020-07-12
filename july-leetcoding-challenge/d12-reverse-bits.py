"""
Reverse bits of a given 32 bits unsigned integer.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        while i < 32:
            res = res*2 + n%2
            n //= 2
            i += 1
        
        return res
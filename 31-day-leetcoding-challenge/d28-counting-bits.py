"""
Given a non negative integer number num. 
For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
"""


class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num+1):
            x = i
            bits = 0
            while x > 0:
                if x % 2 == 1:
                    bits += 1
                x = x//2
            res.append(bits)
        return res
"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hd = 0
        while x or y:
            if x%2 != y%2:
                hd += 1
            x //= 2
            y //= 2
        return hd
"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
"""


class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        s = 0
        while num:
            s += num%10
            num //= 10
        return self.addDigits(s)
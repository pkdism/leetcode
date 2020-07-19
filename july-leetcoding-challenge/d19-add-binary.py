"""
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l1, l2 = len(a), len(b)
        
        i, j = l1 - 1, l2 - 1
        res = ""
        c = 0
        while i >= 0 or j >= 0:
            s = 0
            if i >= 0:
                s += int(a[i])
                i -= 1
            if j >= 0:
                s += int(b[j])
                j -=1
            s += c
            
            res = str(s%2) + res
            c = s//2
        
        if c == 1:
            res = "1" + res
        
        return res
            
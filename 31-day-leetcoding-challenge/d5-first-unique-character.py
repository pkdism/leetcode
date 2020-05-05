"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1. 
"""


from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        return -1
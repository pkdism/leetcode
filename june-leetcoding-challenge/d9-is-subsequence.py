"""
Given a string s and a string t, check if s is subsequence of t.
A subsequence of a string is a new string which is formed from the 
original string by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters. 
(ie, "ace" is a subsequence of "abcde" while "aec" is not).
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        if n1 == 0:
            return True
        if n1 > n2:
            return False
        
        i, j = 0, 0
        while i < n1 and j < n2:
            print(i, j, s[i], t[j])
            if s[i] == t[j]:
                i += 1
            j += 1
        
        if i < n1:
            return False
        return True
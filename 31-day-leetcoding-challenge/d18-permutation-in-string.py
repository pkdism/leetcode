"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.
"""


class Solution:
    
    def is_permutation(self, h1, h2):
        for i in range(26):
            if h1[i] != h2[i]:
                return False
        return True
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        
        if l1 > l2:
            return False
        
        c1, c2 = [0]*26, [0]*26
        
        for x in s1:
            c1[ord(x) - ord('a')] += 1
        
        for i in range(l1):
            c2[ord(s2[i]) - ord('a')] += 1
            
        flag = self.is_permutation(c1, c2)
        if flag:
            return True
        
        for i in range(1, l2-l1+1):
            c2[ord(s2[i-1]) - ord('a')] -= 1
            c2[ord(s2[i+l1-1]) - ord('a')] += 1
            flag = self.is_permutation(c1, c2)
            if flag:
                return True
        return False
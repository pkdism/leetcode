"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.
"""


from collections import Counter
class Solution:
    def is_anagram(self, cs, cp):
        for i in range(26):
            if cs[i] != cp[i]:
                return False
        return True
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counts = [0]*26
        for x in p:
            counts[ord(x) - ord('a')] += 1
        
        plen = len(p)
        slen = len(s)
        res = []
        
        s0 = s[:plen]
        
        scounts = [0]*26
        
        for x in s0:
            scounts[ord(x) - ord('a')] += 1
        
        print(scounts)
        
        if self.is_anagram(scounts, counts):
            res.append(0)

        for i in range(1, slen - plen + 1):
            scounts[ord(s[i-1]) - ord('a')] -= 1
            scounts[ord(s[i + plen - 1]) - ord('a')] += 1

            if self.is_anagram(scounts, counts):
                res.append(i)
        
        return res
"""
Given an array of strings, group anagrams together.
"""


from collections import defaultdict
class Solution:
    
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))    
            groups[sorted_word].append(word)
        
        return list(groups.values())

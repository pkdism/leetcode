"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
add spaces in s to construct a sentence where each word is a valid dictionary word. 
Return all such possible sentences.
Note:
    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        n = len(s)
        all_splits_i = [[] for x in range(n)] + [[""]]
        
        can_split = [0]*n + [1]
        
        for i in range(n):
            for j in range(i, -1, -1):
                if s[j:(i+1)] in word_set:
                    can_split[i] = max(can_split[i], can_split[j-1])
                    
        if can_split[-2] == 0:
            return []
        
        for i in range(n):
            for j in range(i, -1, -1):
                if s[j:(i+1)] in word_set:
                    for x in all_splits_i[j-1]:
                        all_splits_i[i].append(x + " " + s[j:(i+1)])
        
        return [s[1:] for s in all_splits_i[-2]]
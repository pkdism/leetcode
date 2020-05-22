"""
Given a string, sort it in decreasing order based on the frequency of characters.
"""


from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        return ''.join([x[0]*x[1] for x in (sorted(c.items(), key = lambda k: -k[1]))])
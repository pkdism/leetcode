"""
Given an input string, reverse the string word by word.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([x for x in list(reversed(s.split(' '))) if x != ''])
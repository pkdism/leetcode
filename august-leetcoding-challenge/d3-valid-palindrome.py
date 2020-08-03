"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for x in s:
            if x.isalnum():
                t = t + x.lower()
        return t == ''.join(list(reversed(t)))
"""
 Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
    An empty string is also valid.
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        l, h = 0, 0
        for c in s:
            if c == '(':
                l += 1
            else:
                l -= 1
            if c != ')':
                h += 1
            else:
                h -= 1
            if h < 0:
                return False
            l = max(l, 0)
        return l == 0
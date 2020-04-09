"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
"""


class Solution:

    def getString(self, S):
        q = []
        n = len(S)
        res = ''
        for i in range(n):
            if S[i] != '#':
                q.append(S[i])
            elif len(q) > 0:
                q.pop()
        
        while len(q) > 0:
            res += q[0]
            q.pop(0)
        
        return res
    
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.getString(S) == self.getString(T)
        
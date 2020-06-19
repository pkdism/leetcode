"""
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)
Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)
"""


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        def searchString(m, mod):
            hsh = 0
            for i in range(m):
                hsh = (hsh * 26 + vals[i]) % mod
            s = {hsh}
            p = pow(26, m, mod)
            for i in range(1, n - m + 1):
                hsh = (hsh * 26 - vals[i - 1] * p + vals[i + m - 1]) % mod
                if hsh in s:
                    return i
                s.add(hsh)
            return -1

        n = len(S)
        vals = [ord(c) - ord('a') for c in S]
        l = 1
        r = n
        i = -1
        mod = 2**63 - 1
        while l <= r:
            m = l + (r-l)//2
            pattern = searchString(m, mod)
            if pattern != -1:
                l = m + 1
                i = pattern
            else:
                r = m - 1
        return S[i: i + l - 1]
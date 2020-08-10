class Solution:
    def titleToNumber(self, s: str) -> int:
        n = len(s)
        res = 0
        power = n-1
        for x in s:
            coeff = ord(x) - ord('A') + 1
            res += coeff * (26**power)
            power -= 1
        return res
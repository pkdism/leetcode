class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        c = 0
        s = set(J)
        for x in S:
            if x in s:
                c += 1
        return c
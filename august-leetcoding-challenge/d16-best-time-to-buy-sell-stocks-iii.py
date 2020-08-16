class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b1 = float(-inf)
        s1 = 0
        b2 = float(-inf)
        s2 = 0
        for price in prices:
            b1 = max(b1, -price)
            s1 = max(s1, b1 + price)
            b2 = max(b2, s1 - price)
            s2 = max(s2, b2 + price)
        return s2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_price = prices[n-1]
        max_profit = 0
        for i in range(n-2, -1, -1):
            profit = max_price - prices[i]
            max_profit = max(profit, max_profit)
            max_price = max(max_price, prices[i])
        return max_profit

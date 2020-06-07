"""
You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.
"""


class Solution:    
    
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        dp = [[0]*(amount+1) for _ in range(n + 1)]
        
        dp[0][0] = 1
        
        for c in range(1, n + 1):
            dp[c][0] = 1
            for a in range(1, amount + 1):
                dp[c][a] = dp[c-1][a]
                if a - coins[c-1] >= 0:
                    dp[c][a] += dp[c][a-coins[c-1]]
                    
        return dp[n][amount]
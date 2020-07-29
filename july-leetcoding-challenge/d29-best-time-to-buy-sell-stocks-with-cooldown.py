"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cool = 0
        sell = 0
        hold = -float('inf')
        
        for d in prices:
            pcool = cool
            psell = sell
            phold = hold
            
            cool = max(pcool, psell)
            sell = phold + d
            hold = max(phold, pcool - d)
        
        return max(sell, cool)
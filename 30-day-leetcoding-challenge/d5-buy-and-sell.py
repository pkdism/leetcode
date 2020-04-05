"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions 
as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""


class Solution:
    def maxProfit(self, a: List[int]) -> int:
        profit = 0
        n = len(a)
        if n <= 1:
            return profit
        minima = 0
        i = 0
        while True:
            while i < n - 1 and a[i+1] <= a[i]:
                i += 1
            if i == n - 1:
                return profit

            minima = a[i]
        
            while i < n - 1 and a[i+1] >= a[i]:
                i += 1
                
            profit += (a[i] - minima)
            if i < n - 1:
                minima = a[i+1]
        return profit
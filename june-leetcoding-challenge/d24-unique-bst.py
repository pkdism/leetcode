"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
"""


class Solution:
    def numTrees(self, n: int) -> int:
        res = factorial(2*n)
        res //= factorial(n)
        res //= factorial(n)
        res //= (n+1)
        return res
"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
"""


from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        root = sqrt(n)
        squares = [x*x for x in range(int(root) + 1)]
        
        if n in squares:
            return 1
        
        for n1 in squares:
            if n - n1 in squares:
                return 2
            
        for n1 in squares:
            for n2 in squares:
                if n - n1 - n2 in squares:
                    return 3
        
        return 4
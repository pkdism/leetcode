"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        if len(matrix) == 0:
            return 0
        elif len(matrix[0]) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        
        res = [[0 for i in range(n)] for i in range(m)]
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                res[i][j] = min(res[i-1][j-1], res[i][j-1], res[i-1][j]) + 1 if matrix[i][j] == '1' else 0
                max_area = max(res[i][j], max_area)
        
        return max_area**2
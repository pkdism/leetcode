"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
"""


class Solution:
    
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        row, col = len(matrix), len(matrix[0])
        
        c = 0
        
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0:
                    c += matrix[i][j]
                else:
                    if matrix[i][j] == 1:
                        val = min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]) + 1
                        matrix[i][j] = val
                        c += val
        
        return c
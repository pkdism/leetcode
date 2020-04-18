"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                elif r == 0:
                    grid[r][c] += grid[r][c-1]
                elif c == 0:
                    grid[r][c] += grid[r-1][c]
                else:
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        return grid[m-1][n-1]
        
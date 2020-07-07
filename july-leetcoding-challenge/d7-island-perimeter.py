"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). 
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.
"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                p += 4*grid[i][j]
                if i > 0:
                    p -= grid[i][j]*grid[i-1][j]
                if i < rows-1:
                    p -= grid[i][j]*grid[i+1][j]
                if j > 0:
                    p -= grid[i][j]*grid[i][j-1]
                if j < cols-1:
                    p -= grid[i][j]*grid[i][j+1]
        return p
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        s = set()
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    s.add((i, j))
                    
        def explore(i, j):
            if (i, j) in s:
                s.remove((i, j))
                explore(i + 1, j)
                explore(i - 1, j)
                explore(i, j + 1)
                explore(i, j - 1)
        
        while s:
            cur = s.pop()
            s.add(cur)
            
            explore(cur[0], cur[1])
            islands += 1
        return islands
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rotten = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add("" + str(i) + str(j))
                elif grid[i][j] == 2:
                    rotten.add("" + str(i) + str(j))
        
        minutes = 0
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while len(fresh) > 0:
            infected = set()
            for s in rotten:
                i = int(s[0])
                j = int(s[1])
                for direction in directions:
                    nexti = i + direction[0]
                    nextj = j + direction[1]
                    temp = str(nexti) + str(nextj)
                    if temp in fresh:
                        fresh.remove(temp)
                        infected.add(temp)
            if len(infected) == 0:
                return -1
            rotten = infected
            minutes += 1
        return minutes
                    
        
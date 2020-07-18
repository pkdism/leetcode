"""
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.adj_list = defaultdict(set)
        for pair in prerequisites:
            self.adj_list[pair[0]].add(pair[1])
        
        self.visited = [0]*numCourses
        self.res = []
        self.cycle = 0
        
        for x in range(numCourses):
            if self.cycle == 1:
                break
            if self.visited[x] == 0:
                self.dfs(x)
                
        if self.cycle == 1:
            return []
        else:
            return self.res
        
    def dfs(self, start):
        if self.cycle == 1:
            return
        if self.visited[start] == 1:
            self.cycle = 1
        if self.visited[start] == 0:
            self.visited[start] = 1
            for n in self.adj_list[start]:
                self.dfs(n)
            self.visited[start] = 2
            self.res.append(start)
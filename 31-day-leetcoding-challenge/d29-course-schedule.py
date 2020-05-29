"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        connections = [[] for _ in range(numCourses)]
        
        for u, v in prerequisites:
            connections[u].append(v)
        
        for start in range(numCourses):
            visited = [False for _ in range(numCourses)]
            nums = [start]
            while len(nums) > 0:
                top = nums.pop()
                if not visited[top]:
                    nums.extend(connections[top])
                elif top == start:
                    return False
                visited[top] = True
        return True
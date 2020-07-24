"""
Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.
The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.
"""


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def explore(ls):
            if ls[-1] == n-1:
                res.append(ls)
                return
            for x in graph[ls[-1]]:
                explore(ls + [x])
                
            
        n = len(graph)
        res = []
        explore([0])
        return res
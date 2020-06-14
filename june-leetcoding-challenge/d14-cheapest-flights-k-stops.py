"""
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
Now given all the cities and flights, together with starting city src and the destination dst, 
your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
"""


from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        g = defaultdict(list)
        d = deque([[src, 0, 0]])
        
        m = float('inf')
        
        for u, v, w in flights:
            g[u].append([v, w])
            
        while d:
            u, v, w = d.popleft()
            
            if w <= m and v <= K and u != dst:
                for vd, wd in g[u]:
                    d.append([vd, v + 1, w + wd])
            
            if u == dst:
                m = min(m, w)
                
        if m != float('inf'):
            return m
        else:
            return -1
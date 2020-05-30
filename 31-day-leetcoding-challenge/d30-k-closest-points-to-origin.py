"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
"""


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = {}
        n = len(points)
        for i in range(n):
            point = points[i]
            dist[i] = dist.get(i, point[0]*point[0] + point[1]*point[1])
        
        sorted_dist = {k: v for k, v in sorted(dist.items(), key = lambda item: item[1])}
        
        k = 0
        res = []
        for idx in sorted_dist.keys():
            if k >= K:
                break
            res.append(points[idx])
            k += 1
        return res
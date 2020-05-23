"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.
For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
"""


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        len_a = len(A)
        len_b = len(B)
        
        i, j = 0, 0
        res = []
        while i < len_a and j < len_b:
            start_a, end_a = A[i][0], A[i][1]
            start_b, end_b = B[j][0], B[j][1]
            
            start_res = max(start_a, start_b)
            end_res = min(end_a, end_b)
            
            if start_res <= end_res:
                res.append([start_res, end_res])
                
            if end_a >= end_b:
                j += 1
            else:
                i += 1
        
        return res
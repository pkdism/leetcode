"""
We write the integers of A and B (in the order they are given) on two separate horizontal lines.
Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:
    A[i] == B[j];
    The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.
Return the maximum number of connecting lines we can draw in this way.
"""


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        na, nb = len(A), len(B)
        
        res = [[0]*(nb+1) for _ in range(na+1)]
        
        for i in range(na):
            for j in range(nb):
                if A[i] == B[j]:
                    res[i+1][j+1] = res[i][j] + 1
                else:
                    res[i+1][j+1] = max(res[i][j+1], res[i+1][j])
        
        return res[na][nb]
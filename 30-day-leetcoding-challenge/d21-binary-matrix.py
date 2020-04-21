"""
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.
Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.
"""


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dims = binaryMatrix.dimensions()
        m, n = dims[0], dims[1]
        min_col = inf
        for i in range(m):
            low, high = 0, n-1
            while low <= high:
                mid = (low+high)//2
                if binaryMatrix.get(i, mid) == 1:
                    min_col = min(min_col, mid)
                    high = mid - 1
                else:
                    low = mid + 1
        if min_col > n:
            return -1
        return min_col
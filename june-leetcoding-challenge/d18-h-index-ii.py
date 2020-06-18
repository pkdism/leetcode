"""
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, 
write a function to compute the researcher's h-index.
According to the definition of h-index on Wikipedia: 
"A scientist has index h if h of his/her N papers have at least h citations each, 
and the other N − h papers have no more than h citations each."
"""


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 0:
            return 0
        n = len(citations)
        start, end = 0, n - 1
        while start <= end:
            m = start + (end - start)//2
            if m + citations[m] >= n:
                end = m - 1
            else:
                start = m + 1
        return n - start
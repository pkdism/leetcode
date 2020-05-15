"""
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.
Here, a circular array means the end of the array connects to the beginning of the array.  
(Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)
Also, a subarray may only include each element of the fixed buffer A at most once.  
(Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
"""


class Solution:
    
    def kadanes(self, A):
        n = len(A)
        overall_max, cur_max = 0, 0
        for i in range(n):
            cur_max += A[i]
            if cur_max < 0:
                cur_max = 0
            overall_max = max(overall_max, cur_max)
        return overall_max
    
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        flag = True
        for x in A:
            if x >= 0:
                flag = False
                break
        if flag == True:
            return max(A)
        
        
        n = len(A)
        
        m1 = self.kadanes(A)
        
        m2 = 0
        for i in range(n):
            m2 += A[i]
            A[i] = -A[i]
        
        m2 += self.kadanes(A)
        
        overall_max = max(m1, m2)

        return max(overall_max, 0)
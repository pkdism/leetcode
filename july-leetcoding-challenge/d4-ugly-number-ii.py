"""
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
"""


class Solution:

    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        f2, f3, f5 = 0, 0, 0
        uglies = [0]*n
        uglies[0] = 1
        for i in range(1, n):
            uglies[i] = min(uglies[f2]*2, uglies[f3]*3, uglies[f5]*5)
            if uglies[i] == uglies[f2]*2:
                f2 += 1
            if uglies[i] == uglies[f3]*3:
                f3 += 1
            if uglies[i] == uglies[f5]*5:
                f5 += 1
        return uglies[n-1]
"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        c = 1
        
        n = len(digits)
        
        for i in range(n-1, -1, -1):
            s = digits[i] + c
            digits[i] = s%10
            c = s//10
            print(s, c, digits[i])
        
        if c == 0:
            return digits
        else:
            res = []
            res.append(c)
            res.extend(digits)
            return res
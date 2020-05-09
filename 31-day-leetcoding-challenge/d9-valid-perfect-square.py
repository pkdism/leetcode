"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        low = 1
        high = num//2
        
        while low <= high:
            mid = (low + high)//2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1
                
        return False
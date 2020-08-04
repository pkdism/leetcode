"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
"""


from math import log
class Solution:
    
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        # while num:
        #     if num == 1:
        #         return True
        #     if num % 4 != 0:
        #         return False
        #     num = num >> 2
        # return True
        
        # return log(num, 4)%1.0 == 0
        
        return num & (num-1) == 0 and (num-1)%3 == 0
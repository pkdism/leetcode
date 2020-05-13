"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
Note:
    The length of num is less than 10002 and will be ≥ k.
    The given num does not contain any leading zero.
"""


class Solution:
    reduced_string = ""
    
    def removeKdigits(self, num: str, k: int) -> str:
        
        if k == 0:
            self.reduced_string += num
            if len(self.reduced_string) == 0:
                return "0"
            else:
                return self.reduced_string
        
        n = len(num)
        
        if n <= k:
            if len(self.reduced_string) == 0:
                return "0"
            else:
                return self.reduced_string
        
        idx = 0
        
        for i in range(1, k+1):
            if int(num[i]) < int(num[idx]):
                idx = i
        
        self.reduced_string += num[idx]
        
        
        self.removeKdigits(num[(idx+1):], k-idx)
        return str(int(self.reduced_string))
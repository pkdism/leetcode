"""
Given an array w of positive integers, 
where w[i] describes the weight of index i, 
write a function pickIndex which randomly picks an index in proportion to its weight.
"""


import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.n = len(self.w)
        self.arr = []
        self.curr = 0
        for x in w:
            self.curr += x
            self.arr.append(self.curr)
        
        

    def pickIndex(self) -> int:
        # print(self.arr)
        n = len(self.arr)
        r = random.randrange(1, self.arr[-1] + 1)
        l = 0
        h = n-1
        while l < h:
            m = (l+h)//2
            # if self.arr[m] == r:
                # return m
            if self.arr[m] < r:
                l = m + 1
            else:
                h = m
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
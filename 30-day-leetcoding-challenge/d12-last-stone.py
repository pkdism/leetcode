"""
We have a collection of stones, each stone has a positive integer weight.
Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

    If x == y, both stones are totally destroyed;
    If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
"""


class Solution:
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while True:
            
            count = 0
            index = 0
            for i in range(len(stones)):
                if stones[i] != -1:
                    count += 1
                    index = i
            
            if count == 0:
                return 0
            
            if count == 1:
                return stones[index]
            
            m1, m2 = 0, 0
            i1, i2 = 0, 0
            cur_max = 0
            
            for i in range(len(stones)):
                if stones[i] != -1:
                    cur_max = max(cur_max, stones[i])
                    if cur_max > m1:
                        m1 = cur_max
                        i1 = i
            
            cur_max = 0
            
            for i in range(len(stones)):
                if stones[i] != -1:
                    if i != i1:
                        cur_max = max(cur_max, stones[i])
                        if cur_max > m2:
                            m2 = cur_max
                            i2 = i
            
            if stones[i1] == stones[i2]:
                stones[i1] = -1
                stones[i2] = -1
            else:
                stones[i1] -= stones[i2]
                stones[i2] = -1
            
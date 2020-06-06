"""
Suppose you have a random list of people standing in a queue. 
Each person is described by a pair of integers (h, k), 
where h is the height of the person and k is the number of 
people in front of this person who have a height greater than or equal to h. 
Write an algorithm to reconstruct the queue.
"""


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        
        sorted_p = list(sorted(people, key = lambda k: (-k[0], k[1])))
        res = []
        for x in sorted_p:
            res.insert(x[1], x)
        
        return res
"""
Given a non-empty array of integers, return the k most frequent elements.
"""


from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        s = {k: v for k, v in sorted(c.items(), key = lambda x: -x[1])}
        res = []
        for key, v in s.items():
            res.append(key)
            k -= 1
            if k <= 0:
                break
        return res
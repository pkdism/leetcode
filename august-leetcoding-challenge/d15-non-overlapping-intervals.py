class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[1])
        # print(intervals)
        n = len(intervals)
        if n <= 1:
            return 0
        current_end = intervals[0]
        res = 1
        
        for i in range(n):
            if intervals[i][0] >= current_end[1]:
                # print(intervals[i])
                current_end = intervals[i]
                res += 1
        
        return n - res
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n == 0:
            return 0
        
        res = 0
        citations.sort(reverse = True)
        
        if citations[n-1] >= len(citations):
            return n
        
        for i in range(1, n+1):
            if i > citations[i-1]:
                res = i - 1
                break
        
        return res
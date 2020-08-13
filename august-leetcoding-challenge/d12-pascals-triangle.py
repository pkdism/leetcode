class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tri = []
        tri.append([1])
        
        for i in range(2, rowIndex+2):
            row = [None]*i
            for j in range(0, i):
                if j == 0 or j == i-1:
                    row[j] = 1
                else:
                    row[j] = tri[-1][j-1] + tri[-1][j]
            tri.append(row)
        print(tri[-1])
        return tri[-1]
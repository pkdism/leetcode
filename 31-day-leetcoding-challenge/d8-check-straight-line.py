"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] 
represents the coordinate of a point. Check if these points make a straight line in the XY plane.
"""


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        n = len(coordinates)
        flag_x, flag_y = 0, 0
        
        for i in range(1, n):
            if coordinates[i][1] != coordinates[0][1]:
                flag_y = 1
                break        
        if flag_y == 0:
            return True
        
        for i in range(1, n):
            if coordinates[i][0] != coordinates[0][0]:
                flag_x = 1
                break 
        if flag_y == 0:
            return True
        
        x1, x2 = coordinates[0][0], coordinates[1][0]
        y1, y2 = coordinates[0][1], coordinates[1][1]
        
        if x2 - x1 == 0:
            return False
        
        m = (y2 - y1)/(x2 - x1)
        
        for i in range(2, n):
            xi, yi = coordinates[i][0], coordinates[i][1]
            if xi - x1 == 0:
                return False
            mi = (yi - y1)/(xi - x1)
            if mi != m:
                return False
            
        return True
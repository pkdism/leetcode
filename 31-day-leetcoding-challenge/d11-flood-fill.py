"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
At the end, return the modified image. 
"""


class Solution:
    
    image = [[None]*50 for _ in range(50)]
    
    
    def helper(self, sr, sc, color, newColor): 
        
        n = len(self.image)
        m = len(self.image[0])
        
        flag = (sr < 0 or sr >= n or sc < 0 or sc >= m or self.image[sr][sc] != color or self.image[sr][sc] == newColor)
        
        if flag: 
            return

        self.image[sr][sc] = newColor 

        self.helper(sr + 1, sc, color, newColor) 
        self.helper(sr - 1, sc, color, newColor) 
        self.helper(sr, sc + 1, color, newColor) 
        self.helper(sr, sc - 1, color, newColor) 
    
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        self.image = image
        self.helper(sr, sc, image[sr][sc], newColor)
        return self.image
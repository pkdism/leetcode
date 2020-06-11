"""
Given an array with n objects colored red, white or blue, 
sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones, twos = 0, 0, 0
        for x in nums:
            if x == 0:
                zeros += 1
            elif x == 1:
                ones += 1
            else:
                twos += 1
            
        i = 0                
        while zeros > 0:
            nums[i] = 0
            zeros -= 1
            i += 1
            
        while ones > 0:
            nums[i] = 1
            ones -= 1
            i += 1
            
        while twos > 0:
            nums[i] = 2
            twos -= 1
            i += 1
        
        return nums
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""


class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)        
        
        def binarySearch(low, high):
            if high < low:
                return -1
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(low, mid-1)
            return binarySearch(mid+1, high)
        
        def findPivot(low, high):
            if high < low:
                return -1
            if high == low:
                return low
            mid = (low + high)//2
            if mid < high and nums[mid] > nums[mid+1]:
                return mid
            if mid > low and nums[mid-1] > nums[mid]:
                return (mid-1)
            elif nums[low] >= nums[mid]:
                return findPivot(low, mid-1)
            return findPivot(mid+1, high)
        
        pivot = findPivot(0, n-1)
        if pivot == -1:
            return binarySearch(0, n-1)
        if nums[pivot] == target:
            return pivot
        elif nums[0] <= target:
            return binarySearch(0, pivot-1)
        return binarySearch(pivot+1, n-1)
            
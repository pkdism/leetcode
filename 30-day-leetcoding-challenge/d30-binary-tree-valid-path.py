"""
Given a binary tree where each path going from the root to any leaf form a valid sequence, 
check if a given string is a valid sequence in such binary tree. 

We get the given string from the concatenation of an array of integers arr and the 
concatenation of all values of the nodes along a path results in a sequence in the given binary tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def validPath(self, root, arr, index, n):
        if root is None:
            if n == 0:
                return True
            else:
                return False
            
        if root.left is None and root.right is None and index == n-1 and root.val == arr[index]:
            return True
        
        if index < n and root.val == arr[index]:
            left = self.validPath(root.left, arr, index + 1, n)
            right = self.validPath(root.right, arr, index + 1, n)
            return left or right
        else:
            return False
    
    
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        
        return self.validPath(root, arr, 0, len(arr))
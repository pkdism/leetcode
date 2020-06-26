"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def util(self, root, s):
        if root is None:
            return 0
        s = 10*s + root.val
        if root.left is None and root.right is None:
            return s
        return self.util(root.left, s) + self.util(root.right, s)    
    
    def sumNumbers(self, root: TreeNode) -> int:
        return self.util(root, 0)
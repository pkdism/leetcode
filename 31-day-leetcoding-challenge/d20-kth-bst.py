"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    count = 0
    kth = 0
    
    def inorderTraversal(self, root, k):
        if root is None:
            return
        self.kthSmallest(root.left, k)
        self.count += 1
        if self.count == k:
            self.kth = root.val
            return
        self.kthSmallest(root.right, k)        
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.inorderTraversal(root, k)
        return self.kth
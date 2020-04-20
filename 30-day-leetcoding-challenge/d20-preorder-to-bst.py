"""
Return the root node of a binary search tree that matches the given preorder traversal.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        n = len(preorder)
        
        if n == 0:
            return None
        
        root = TreeNode(preorder[0])
        
        i = 1
        while i < n and preorder[i] < root.val:
            i += 1
            
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        
        return root
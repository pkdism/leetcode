"""
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root. 
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def path_length(self, root):
        if root == None:
            return 0
        else:
            return 1 + max(self.path_length(root.left), self.path_length(root.right))
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
    
        return max(self.diameterOfBinaryTree(root.left),
                   self.diameterOfBinaryTree(root.right),
                   self.path_length(root.left) + self.path_length(root.right))
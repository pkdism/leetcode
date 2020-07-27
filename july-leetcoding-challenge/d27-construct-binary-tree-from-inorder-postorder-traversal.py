"""
Given inorder and postorder traversal of a tree, construct the binary tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.buildTreeUtil(inorder, postorder, 0, len(inorder) - 1, len(postorder) - 1)
    
    def buildTreeUtil(self, inorder, postorder, start, end, root_index):
        if start > end:
            return None
        tree = TreeNode(postorder[root_index])
        
        inorder_index = 0
        
        while inorder[inorder_index] != postorder[root_index]:
            inorder_index += 1
        
        tree.right = self.buildTreeUtil(inorder, postorder, inorder_index+1, end, root_index - 1)
        tree.left = self.buildTreeUtil(inorder, postorder, start, inorder_index-1, root_index - (end - inorder_index) - 1)
        return tree
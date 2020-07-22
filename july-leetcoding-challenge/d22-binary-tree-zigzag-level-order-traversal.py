"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        iter = [root] if root else None
        res = []
        sign = True
        
        while iter:
            level = [node.val for node in (iter if sign else reversed(iter))]
            res.append(level)
            next_node = []
            for node in iter:
                if node.left: next_node.append(node.left)
                if node.right: next_node.append(node.right)
            iter = next_node
            sign = not sign
        
        return res
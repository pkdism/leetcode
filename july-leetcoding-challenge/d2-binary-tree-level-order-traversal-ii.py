"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, root, level):
        if root is None:
            return
        if level not in self.traversal:
            self.traversal[level] = []
        self.traversal[level].append(root.val)
        self.traverse(root.left, level + 1)
        self.traverse(root.right, level + 1)
        
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.traversal = defaultdict(list)
        self.traverse(root, 0)
        res = list(reversed([v for k, v in self.traversal.items()]))
        return res
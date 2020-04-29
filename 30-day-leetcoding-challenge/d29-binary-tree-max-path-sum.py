"""
Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node
to any node in the tree along the parent-child connections. The path must contain at
least one node and does not need to go through the root.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    max_sum = -inf
    
    def sum_tree(self, root):
        if root is None:
            return 0
        else:
            left_sum = self.sum_tree(root.left)
            right_sum = self.sum_tree(root.right)

            self.max_sum = max(self.max_sum,
                               left_sum + right_sum + root.val,
                               root.val,
                               root.val + left_sum,
                               root.val + right_sum,
                               root.val + left_sum + right_sum)

            return max(left_sum, right_sum, 0) + root.val
    
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.sum_tree(root)
        return self.max_sum

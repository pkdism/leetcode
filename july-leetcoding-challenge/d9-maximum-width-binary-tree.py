"""
Given a binary tree, write a function to get the maximum width of the given tree. 
The width of a tree is the maximum width among all levels. 
The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes 
(the leftmost and right most non-null nodes in the level, where the null 
nodes between the end-nodes are also counted into the length calculation.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        parent_level = 1
        parent_node = 1
        width = 0
        
        q = deque([[parent_level, parent_node, root]])
        
        while len(q) > 0:
            [curr_node, curr_level, node] = q.popleft()
            if curr_level > parent_level:
                parent_level, parent_node = curr_level, curr_node
            width = max(width, curr_node - parent_node + 1)
            if node.left is not None:
                q.append([curr_node*2, curr_level + 1, node.left])
            if node.right is not None:
                q.append([curr_node*2+1, curr_level + 1, node.right])
        
        return width
"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def checkSiblings(self, root, x, y):
        if root is None:
            return False
        left_val = -1
        if root.left is not None:
            left_val = root.left.val
        right_val = -2
        if root.right is not None:
            right_val = root.right.val
        if (left_val == x and right_val == y) or (left_val == y and right_val == x):
            return True
        return self.checkSiblings(root.left, x, y) or self.checkSiblings(root.right, x, y)
        
    
    def getDepth(self, root, node_val, d):
        
        if root is None:
            return -1
        elif root.val == node_val:
            print("elif", root.val, d)
            return d
        else:
            print("else", root.val, d)
            return max(self.getDepth(root.left, node_val, d + 1), self.getDepth(root.right, node_val, d + 1))
        
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xd = self.getDepth(root, x, 0)
        print("")
        yd = self.getDepth(root, y, 0)
        print("")
        print(xd, yd)
        print("")
        print(self.checkSiblings(root, x, y))
        if xd != -1 and yd != -1:
            if xd == yd:
                s = self.checkSiblings(root, x, y)
                if s is True:
                    return False
                else:
                    return True
        return False
        
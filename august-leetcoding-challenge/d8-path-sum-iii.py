# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def cumulative_sum(self, root):
        self.n += 1
        for x in filter(None, [root.left, root.right]):
            x.val += root.val
            self.cumulative_sum(x)
                
    def dfs(self, root, sum):
        if not root: 
        	return None
        
        self.count[root.val + sum] += 1
        self.res += self.count[root.val]
        self.dfs(root.left, sum)
        self.dfs(root.right, sum)
        self.count[root.val + sum] -= 1
 
    def pathSum(self, root, sum):
        if not root: 
        	return 0
        
        self.n, self.res, self.count = 0, 0, defaultdict(int)
        self.cumulative_sum(root)
        self.count[sum] = 1
        self.dfs(root, sum)
        return self.res  - self.n*(sum == 0) 
        
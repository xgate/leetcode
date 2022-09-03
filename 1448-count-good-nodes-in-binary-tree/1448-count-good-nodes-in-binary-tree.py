# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, maxVal):
        if not node: return 0        
        c = 1 if node.val >= maxVal else 0
        lc = self.dfs(node.left, max(maxVal, node.val))
        rc = self.dfs(node.right, max(maxVal, node.val))        
        return c + lc + rc
    
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)

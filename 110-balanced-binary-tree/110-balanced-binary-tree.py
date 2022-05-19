# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, h): 
        if not node:
            return h
        lh = self.dfs(node.left, h+1)
        rh = self.dfs(node.right, h+1)
        if lh < 0 or rh < 0:
            return -1
        if abs(lh-rh) > 1:
            return -1
        return max(lh, rh)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        h = self.dfs(root, 0)
        if h < 0:
            return False
        return True

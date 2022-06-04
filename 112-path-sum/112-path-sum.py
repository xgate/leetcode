# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, sum, targetSum):
        if not node.left and not node.right:
            return sum+node.val == targetSum
        if node.left:
            if self.dfs(node.left, sum+node.val, targetSum):
                return True
        if node.right:
            if self.dfs(node.right, sum+node.val, targetSum):
                return True
        return False
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.dfs(root, 0, targetSum)

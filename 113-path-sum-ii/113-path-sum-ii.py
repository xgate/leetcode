# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, targetSum, path, ans):
        if not node.left and not node.right:
            if sum(path) == targetSum:
                ans.append(path.copy())
        if node.left:
            path.append(node.left.val)
            self.dfs(node.left, targetSum, path, ans)
            path.pop()
        if node.right:
            path.append(node.right.val)
            self.dfs(node.right, targetSum, path, ans)
            path.pop()
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = list()
        if not root:
            return ans
        self.dfs(root, targetSum, [root.val], ans)
        return ans

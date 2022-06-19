# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, levelSum, level):
        if levelSum.get(level):
            sum, count = levelSum[level]
            levelSum[level] = (sum+node.val, count+1)
        else:
            levelSum[level] = (node.val, 1)
        if node.left:
            self.dfs(node.left, levelSum, level+1)
        if node.right:
            self.dfs(node.right, levelSum, level+1)
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ls = dict()
        self.dfs(root, ls, 0)
        ans = list()
        for k in sorted(ls.keys()):
            sum, count = ls[k]
            ans.append(round(sum/count, 5))
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, x, depth):
        if node.val == x:
            return depth
        if node.left:
            d = self.dfs(node.left, x, depth+1)
            if d > -1: return d
        if node.right:
            d = self.dfs(node.right, x, depth+1)
            if d > -1: return d
        return -1
    
    def sibling(self, node, x, y):
        if node.left and node.right:
            if (node.left.val == x and node.right.val == y) or (node.left.val == y and node.right.val == x):
                return True
        if node.left:
            if self.sibling(node.left, x, y): return True
        if node.right:
            if self.sibling(node.right, x, y): return True
        return False
    
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        return self.dfs(root, x, -1) == self.dfs(root, y, -1) and not self.sibling(root, x, y)
    
    
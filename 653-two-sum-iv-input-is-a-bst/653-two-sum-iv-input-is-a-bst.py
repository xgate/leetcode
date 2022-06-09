# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def treeToList(self, node, result):
        if not node:
            return
        result.append(node)
        if node.left:
            self.treeToList(node.left, result)
        if node.right:
            self.treeToList(node.right, result)
    
    def find(self, node, n, exclude):
        if not node:
            return False
        if node == exclude:
            return False
        if node.val == n:
            return True
        if node.val < n:
            if self.find(node.right, n, exclude): return True
        else:
            if self.find(node.left, n, exclude): return True
        return False
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nodes = list()
        self.treeToList(root, nodes)
        for i in range(len(nodes)):
            if self.find(root, k-nodes[i].val, nodes[i]):
                return True
        return False

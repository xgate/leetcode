# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def ancestors(self, node, target, result):
        if node.val == target.val:
            result.append(node.val)
            return True
        if node.left:
            if self.ancestors(node.left, target, result):
                result.append(node.val)
                return True
        if node.right:
            if self.ancestors(node.right, target, result):
                result.append(node.val)
                return True
        return False
    
    def find(self, node, val):
        if node.val == val:
            return node
        if node.left:
            found = self.find(node.left, val)
            if found:
                return found
        if node.right:
            found = self.find(node.right, val)
            if found:
                return found
        return None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a1 = list()
        self.ancestors(root, p, a1)
        a2 = list()
        self.ancestors(root, q, a2)        
        d2 = {a2[i]: 1 for i in range(len(a2))}
        for i in range(len(a1)):
            if d2.get(a1[i]):
                break
        
        return self.find(root, a1[i])

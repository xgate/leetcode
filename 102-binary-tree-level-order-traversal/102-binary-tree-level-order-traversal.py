# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, visited, level):
        if visited.get(level):
            visited[level].append(node.val)
        else:
            visited[level] = [node.val]
        if node.left:
            self.dfs(node.left, visited, level+1)
        if node.right:
            self.dfs(node.right, visited, level+1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        vs = dict()
        self.dfs(root, vs, 0)
        return [vs[k] for k in sorted(vs.keys())]

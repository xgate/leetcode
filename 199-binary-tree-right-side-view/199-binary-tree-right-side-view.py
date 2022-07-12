from queue import Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Element:
    def __init__(self, level, node):
        self.level = level
        self.node = node

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        
        nodes = [list() for i in range(100)]
        que = Queue()
        que.put(Element(0, root))
        maxLevel = 0
        while not que.empty():
            element = que.get()
            if element.node.right:
                que.put(Element(element.level+1, element.node.right))
            if element.node.left:
                que.put(Element(element.level+1, element.node.left))
            
            nodes[element.level].append(element.node.val)
            maxLevel = max(maxLevel, element.level)
            
        return [nodes[i][0] for i in range(maxLevel+1)]
    
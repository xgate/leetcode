"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import queue

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        ans = list()
        level = -1
        q = queue.Queue()
        q.put((0, root))
        while not q.empty():
            lv, node = q.get()
            if lv != level: 
                ans.append([node.val])
                level = lv
            else:
                ans[level].append(node.val)                    
            
            for c in node.children: 
                q.put((lv+1, c))
        
        return ans

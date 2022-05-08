# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        que = PriorityQueue()
        for l in lists:
            while l:
                que.put(l.val)
                l = l.next
        
        root = ListNode()
        cursor = root
        while not que.empty():
            cursor.next = ListNode(que.get())
            cursor = cursor.next
            
        return root.next

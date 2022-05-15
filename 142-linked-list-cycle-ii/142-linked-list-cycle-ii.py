# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Two Pointers 
# - meet again continuously on same node.
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        # find cycle
        p1 = head
        p2 = head
        while True:
            p1 = p1.next
            p2 = p2.next
            if not p1 or not p2:
                return None
            p2 = p2.next
            if not p2:
                return None
            if p1 == p2:
                break
                
        # has cycle. find cycle enterance.
        p1 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
            
        return p1

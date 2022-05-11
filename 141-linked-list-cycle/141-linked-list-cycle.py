# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        mark = 10 ** 6
        current = head
        while current:
            if current.val == mark:
                return True
            current.val = mark
            current = current.next
            
        return False

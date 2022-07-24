# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def remove(self, prev, current, nth):
        if not current:
            return False, 1
        removed, depth = self.remove(current, current.next, nth)
        if depth == nth:
            prev.next = current.next
            removed = True
        return removed, depth+1
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        removed, depth = self.remove(head, head.next, n)
        if not removed:
            head = head.next
        return head

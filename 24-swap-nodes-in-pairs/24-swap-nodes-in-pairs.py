# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swap(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: 
            return head
        n1 = head
        n2 = head.next
        nh = n2.next
        
        n2.next = n1
        n1.next = self.swap(nh)
        
        return n2
        
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.swap(head)

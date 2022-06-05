# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, node):
        if not node.next:
            return node
        self.reverse(node.next).next = node
        node.next = None
        return node
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        tail = head
        while tail.next:
            tail = tail.next            
        self.reverse(head)
        return tail

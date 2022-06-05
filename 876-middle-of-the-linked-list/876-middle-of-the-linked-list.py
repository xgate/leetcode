# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head):
        l = 0
        while head:
            head = head.next
            l += 1
        return l
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = self.length(head)
        half = int(len/2)
        for i in range(half):
            head = head.next
        return head
    
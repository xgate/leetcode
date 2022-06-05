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
    
    def findNth(self, head, nth):
        c = 0
        while head:
            if c == nth:
                return head
            head = head.next
            c += 1
    
    def reverse(self, node):
        if not node.next:
            return node
        self.reverse(node.next).next = node
        node.next = None
        return node
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        len = self.length(head)
        if len <= 1:
            return True
        half = int(len/2)
        rhead = head
        while rhead.next:
            rhead = rhead.next
        # half reverse
        self.reverse(self.findNth(head, half))
        # compare
        for i in range(half):
            if head.val != rhead.val:
                return False
            head = head.next
            rhead = rhead.next    
        return True
    
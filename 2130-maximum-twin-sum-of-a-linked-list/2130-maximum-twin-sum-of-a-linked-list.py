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
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        len = self.length(head)
        half = int(len/2)
        rhead = head
        while rhead.next:
            rhead = rhead.next
        # half reverse
        self.reverse(self.findNth(head, half))
        # maxsum
        ans = 0
        for i in range(half):
            ans = max(ans, head.val+rhead.val)
            head = head.next
            rhead = rhead.next
        return ans
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def length(self, head):
        len = 0
        while head:
            len += 1
            head = head.next
        return len
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = self.length(headA)
        lenB = self.length(headB)
        diff = abs(lenA-lenB)
        if lenA > lenB:
            long = headA
            short = headB
        elif lenB > lenA:
            long = headB
            short = headA
        else:
            long = headA
            short = headB
        
        for i in range(diff):
            long = long.next
            if long == short:
                return long
                
        while long and short:
            if long == short:
                return long
            long = long.next
            short = short.next
        
        return None

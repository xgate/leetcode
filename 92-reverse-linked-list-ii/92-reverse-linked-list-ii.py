# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        index = 1
        current = head
        leftNode = rightNode = None
        leftNodeBefore = rightNodeNext = None
        while current:
            if index == left-1:
                leftNodeBefore = current
            if index == left:
                leftNode = current
            if index == right:
                rightNode = current
                rightNodeNext = current.next
                break
            current = current.next
            index += 1
        
        prevNode = leftNode
        current = leftNode.next
        while current and prevNode != rightNode:
            nextNode = current.next
            current.next = prevNode
            
            prevNode = current
            current = nextNode
            
        leftNode.next = rightNodeNext
        if leftNodeBefore:
            leftNodeBefore.next = rightNode
        
        return head if left > 1 else rightNode

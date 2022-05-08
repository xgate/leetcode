# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def fill(self, cursor: ListNode, l: ListNode):
        while l:
            cursor.next = ListNode(l.val)
            l = l.next
            cursor = cursor.next
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: 
            return list2
        if list2 is None:
            return list1
        
        head = ListNode()
        cursor = head
        while list1 and list2:
            val1 = list1.val
            val2 = list2.val
            if val1 >= val2:
                cursor.next = ListNode(val2)
                list2 = list2.next
            else:
                cursor.next = ListNode(val1)
                list1 = list1.next
                
            cursor = cursor.next
        
        
        self.fill(cursor, list1)
        self.fill(cursor, list2)

        return head.next

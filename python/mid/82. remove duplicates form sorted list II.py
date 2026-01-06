# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current:
            has_duplicate = False
            while current.next and current.val == current.next.val:
                has_duplicate = True
                current = current.next  

            if has_duplicate:
              
                prev.next = current.next
            else:
                prev = prev.next 
            current = current.next

        return dummy.next

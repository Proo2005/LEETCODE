# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = []
        while head:
            result.append(str(head.val))  
            head = head.next
        
        binary_str = ''.join(result)     
        return int(binary_str, 2)
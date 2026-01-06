# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Convert nums to a set for O(1) lookup
        remove_set = set(nums)
        
        # Dummy node to simplify edge cases (like removing head)
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
       
        while curr.next:
            if curr.next.val in remove_set:
                curr.next = curr.next.next 
            else:
                curr = curr.next  
                
        return dummy.next

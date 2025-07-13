import heapq
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional['ListNode']]) -> Optional['ListNode']:
        min_heap = []

 
        for idx, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, idx, l))  

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))

        return dummy.next

from collections import deque
from typing import Optional, List
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result: List[List[int]] = []
        q = deque([root])
        left_to_right = True
        
        while q:
            level_size = len(q)
            level = deque()  
            
            for _ in range(level_size):
                node = q.popleft()
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(list(level))
            left_to_right = not left_to_right
        
        return result

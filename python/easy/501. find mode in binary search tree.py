from typing import Optional, List
from collections import Counter

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        vals = []

        def dfs(node):
            if not node:
                return
            vals.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        freq = Counter(vals)
        max_freq = max(freq.values())

        return [k for k,v in freq.items() if v == max_freq]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        r = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            r.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        min_diff = float('inf')
        for i in range(1, len(r)):
            min_diff = min(min_diff, r[i] - r[i - 1])
        
        return min_diff

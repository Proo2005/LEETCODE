# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s=0
        r=[]
        def trav(node):
            if not node:
                return 
            if node.val>=low and node.val<=high:
                r.append(node.val)
            trav(node.left)
            trav(node.right)
        trav(root)

        return sum(r)
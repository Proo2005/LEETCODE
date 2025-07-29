# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        r=[]
        def trav(node):
            if not node:
                return
            r.append(node.val)
            trav(node.left)
            trav(node.right)
        trav(root)

        a=r[0]
        for i in r:
            if i!=a:
                return False
        return True
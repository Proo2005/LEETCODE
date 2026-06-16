# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:

        a = []

        def trav(node):
            if not node:
                return

            a.append(node.val)
            trav(node.left)
            trav(node.right)

        trav(root)

        return a[0] == sum(a[1:])
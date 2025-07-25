# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def order(node):
            if not node:
                return
            order(node.left)
            res.append(node.val)  
            order(node.right)
        order(root)
        return res
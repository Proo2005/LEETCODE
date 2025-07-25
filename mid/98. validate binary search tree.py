class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = [None] 

        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            if prev[0] is not None and node.val <= prev[0]:
                return False
            prev[0] = node.val
            return inorder(node.right)

        return inorder(root)

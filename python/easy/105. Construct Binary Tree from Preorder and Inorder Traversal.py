# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        root_index = inorder.index(root_val)

        left_size = root_index

        root.left = self.buildTree(
            preorder[1:1 + left_size],
            inorder[:root_index]
        )

        root.right = self.buildTree(
            preorder[1 + left_size:],
            inorder[root_index + 1:]
        )

        return root
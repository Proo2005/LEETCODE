# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def dfs(node, path, total):
            if not node:
                return

            path.append(node.val)
            total += node.val

            # Leaf node
            if not node.left and not node.right:
                if total == targetSum:
                    ans.append(path[:])
            else:
                dfs(node.left, path, total)
                dfs(node.right, path, total)

            # Backtrack
            path.pop()

        dfs(root, [], 0)
        return ans
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        matching_nodes_count = 0

        def traverse(node):
            nonlocal matching_nodes_count
            if not node:
                return 0, 0
            left_sum, left_count = traverse(node.left)
            right_sum, right_count = traverse(node.right)
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            if current_sum // current_count == node.val:
                matching_nodes_count += 1
                
            return current_sum, current_count

        traverse(root)
        return matching_nodes_count

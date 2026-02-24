class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total = 0
        stack = [(root, 0)]
        
        while stack:
            node, current = stack.pop()
            current = (current << 1) | node.val
            
            if not node.left and not node.right:
                total += current
            
            if node.left:
                stack.append((node.left, current))
            if node.right:
                stack.append((node.right, current))
        
        return total
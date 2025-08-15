class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def trav(node, curr):
            if not node:
                return 0
            
            curr = curr * 10 + node.val 
            
          
            if not node.left and not node.right:
                return curr
            
         
            return trav(node.left, curr) + trav(node.right, curr)
        
        return trav(root, 0)

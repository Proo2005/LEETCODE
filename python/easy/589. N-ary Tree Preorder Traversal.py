class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        
        def trav(node):
            if not node:
                return
            
            res.append(node.val)
            
            for child in node.children:
                trav(child)
        
        trav(root)
        return res
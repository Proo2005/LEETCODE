class Solution:
    def buildTree(self, inorder, postorder):

        pos = {v:i for i,v in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def build(l, r):
            if l > r:
                return None

            root_val = postorder[self.post_idx]
            self.post_idx -= 1

            root = TreeNode(root_val)
            idx = pos[root_val]

            root.right = build(idx+1, r)
            root.left = build(l, idx-1)

            return root

        return build(0, len(inorder)-1)
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        gs = 0
        def traverse(node):
            nonlocal gs
            if not node:
                return 
            traverse(node.right)
            node.val += gs
            gs = node.val
            traverse(node.left)
        traverse(root)
        return root

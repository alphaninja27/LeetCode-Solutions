class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def ans(root):
            if not root:
                return 0
            return (1 + max(ans(root.left),ans(root.right)))
        if not root:
            return True
        return abs(ans(root.left) - ans(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

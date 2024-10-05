class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        a = float('-inf')
        b = float('inf')
        def check(root, a, b):
            if not root:
                return True
            if root.val <= a or root.val >= b:
                return False
            return check(root.left, a, root.val) and check(root.right, root.val, b)
        return check(root, a, b)

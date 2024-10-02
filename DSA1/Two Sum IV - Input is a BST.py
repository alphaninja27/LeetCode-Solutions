class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        v = {}
        def help(node):
            if not node:
                return False
            if node.val in v:
                return True
            v[k - node.val] = True
            return help(node.left) or help(node.right)
        return help(root)

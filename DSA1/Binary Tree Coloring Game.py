class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        most = (n + 1) // 2
        def dfs(node):
            if not node:
                return False
            if dfs(node.left) or dfs(node.right):
                return True
            isx = node.val == x
            l = node.left.val if node.left else 0
            r = node.right.val if node.right else 0
            if isx and (l >= most or r >= most):
                return True
            node.val = 1 + l + r
            if isx:
                return node.val < most
            return False
        return dfs(root)

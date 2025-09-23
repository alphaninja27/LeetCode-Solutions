class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(x, y):
            if not x.left and not x.right:
                ans.append(y + str(x.val))
                return
            a = y + str(x.val) + "->"
            if x.left:
                dfs(x.left, a)
            if x.right:
                dfs(x.right, a)
        ans = []
        dfs(root, "")
        return ans

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        s = set(to_delete)
        ans = []
        def dfs(root, flag):
            if not root: return None
            dele = (root.val in s)
            root.left = dfs(root.left, dele)
            root.right = dfs(root.right, dele)
            if not dele and flag: ans.append(root)
            return None if dele else root
        dfs(root, True)
        return ans

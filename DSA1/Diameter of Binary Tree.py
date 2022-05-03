class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        r=[0]
        def dfs(root):
            if not root:
                return -1
            left=dfs(root.left)
            right=dfs(root.right)
            r[0]=max(r[0],2+left+right)
            return 1+max(left,right)
        dfs(root)
        return r[0]

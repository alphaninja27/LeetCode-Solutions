class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        rs = [root]
        while rs:
            rv = rs.pop()
            if rv:
                ans.append(rv.val)
                rs.append(rv.right)
                rs.append(rv.left)
        return ans

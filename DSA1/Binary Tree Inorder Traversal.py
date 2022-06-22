class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def help(root):
            if not root:
                return 
            help(root.left)
            ans.append(root.val)
            help(root.right)
        
        help(root)
        return ans

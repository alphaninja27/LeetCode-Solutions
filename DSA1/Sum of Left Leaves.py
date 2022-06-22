class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node, left):
            if not node:
                return
            
            dfs(node.left, True)
            dfs(node.right, False)
            
            if not node.left and not node.right and left:
                self.ans += node.val
                
        dfs(root, False)
        
        return self.ans

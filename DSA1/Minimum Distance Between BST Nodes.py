class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        global ans 
        ans = []
        self.help(root)
        
        return min([ans[i] - ans[i - 1] for i in range(1,len(ans))])
    
    def help(self,root):
        if root:
            self.help(root.left)
            ans.append(root.val)
            self.help(root.right)

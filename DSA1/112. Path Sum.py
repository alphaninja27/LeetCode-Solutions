class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    
        def ans(node, currsum):
            if not node:
                return False
            
            currsum += node.val
            
            if not node.left and not node.right:
                return currsum == targetSum
            
            return (ans(node.left, currsum) or ans(node.right, currsum))
        return ans(root, 0)

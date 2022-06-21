class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.ans(root, low, high, 0)
    
    def ans(self, node, left, right, total):
        if node is None:
            return total
        if left <= node.val <= right:
            total += node.val
            total = self.ans(node.left, left, right, total)
            total = self.ans(node.right, left, right, total)
            
        if node.val < left:
            total = self.ans(node.right, left, right, total)
            
        if node.val > right:
            total = self.ans(node.left, left, right, total)
            
        return total

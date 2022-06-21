class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None or p.val != q.val:
            return False
        else:
            return Solution.isSameTree(self, p.left, q.left) and Solution.isSameTree(self, p.right, q.right)

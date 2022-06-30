class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if s is None and t is None:
                return True
        if t is None:
            return True
        if s is None and t is not None:
            return False
        return self.same(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def same(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        return s.val == t.val and self.same(s.left, t.left) and self.same(s.right, t.right)

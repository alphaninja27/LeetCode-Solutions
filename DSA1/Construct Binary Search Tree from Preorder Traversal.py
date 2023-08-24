class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        if len(preorder) == 1: return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        i = 1
        for j in range(1, len(preorder)):
            if preorder[j] < preorder[0]:
                i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root

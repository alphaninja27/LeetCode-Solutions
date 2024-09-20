# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        ans = 0
        def help(node):
            nonlocal ans
            if node == None:
                return
            help(node.right)
            ans += node.val
            node.val = ans
            help(node.left)
        help(root)
        return root

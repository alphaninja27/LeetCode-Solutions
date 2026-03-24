# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        x_depth = -1
        y_depth = -1
        x_parent = None
        y_parent = None
        prev = None

        def traverse(node, d, parent):
            nonlocal x_depth, y_depth, x_parent, y_parent
            if not node:
                return
            
            if node.val == x:
                x_parent = parent
                x_depth = d
            if node.val == y:
                y_parent = parent
                y_depth = d

            traverse(node.left, d + 1, node)
            traverse(node.right, d + 1, node)
        traverse(root, 1, root)
        return x_depth == y_depth and x_parent!=y_parent

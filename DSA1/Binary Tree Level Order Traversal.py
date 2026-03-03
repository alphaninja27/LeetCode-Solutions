# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lvl = []
        if not root:
            return lvl
        
        def dfs(node, l):
            if not node:
                return
            if len(lvl) == l:
                lvl.append([])
            lvl[l].append(node.val)
            dfs(node.left, l + 1)
            dfs(node.right, l + 1)
        dfs(root, 0)

        return lvl

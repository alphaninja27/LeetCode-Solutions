# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = []
        node = root
        while True:
            while node:
                s.append(node)
                node = node.left
            node = s.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
        

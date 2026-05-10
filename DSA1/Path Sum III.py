# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        def countPath(node, ts):
            if not node:
                return 0
            
            count = 0
            if node.val == ts:
                count += 1
            
            count += countPath(node.left, ts - node.val)
            count += countPath(node.right, ts - node.val)

            return count
        
        return (
            countPath(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
        )

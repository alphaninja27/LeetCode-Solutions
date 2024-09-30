# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        q = deque([root])
        while q:
            temp = deque()
            f = False
            for i in q:
                if not f:
                    ans.append(i.val)
                    f = True
                if i.right:
                    temp.append(i.right)
                if i.left:
                    temp.append(i.left)
            q = temp
        return ans

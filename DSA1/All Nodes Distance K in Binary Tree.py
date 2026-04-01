# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        parent = {}
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            for _ in range(size):
                top = q.popleft()
                if top.left:
                    parent[top.left.val] = top
                    q.append(top.left)
                if top.right:
                    parent[top.right.val] = top
                    q.append(top.right)
        vis = {}
        q.append(target)
        while k > 0 and q:
            size = len(q)
            for _ in range(size):
                top = q.popleft()
                vis[top.val] = 1
                if top.left and top.left.val not in vis:
                    q.append(top.left)
                if top.right and top.right.val not in vis:
                    q.append(top.right)
                if top.val in parent and parent[top.val].val not in vis:
                    q.append(parent[top.val])
            k -= 1
        while q:
            ans.append(q.popleft().val)
        return ans

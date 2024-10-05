class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        ans = 0
        g = defaultdict(list)
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                l, r = node.left, node.right
                if l:
                    g[l.val].append(node.val)
                    g[node.val].append(l.val)
                if r:
                    g[r.val].append(node.val)
                    g[node.val].append(r.val)
                q.append(l)
                q.append(r)
        q.append((start, 0))
        v = set()
        v.add(start)
        while q:
            node, dist = q.popleft()
            for n in g[node]:
                if n not in v:
                    v.add(n)
                    q.append((n, dist + 1))
                ans = dist
        return ans

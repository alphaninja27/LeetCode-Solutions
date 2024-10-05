class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        q = deque()
        v = set()
        ban = set(forbidden)
        j = 0
        q.append((0, True))
        maxi = a + b + max(x, max(forbidden))
        while q:
            s = len(q)
            for i in range(s):
                curr, back = q.popleft()
                if curr == x:
                    return j
                f = (curr + a, True)
                bw = (curr - b, False)
                if f[0] not in ban and f[0] <= maxi and f not in v:
                    q.append(f)
                    v.add(f)
                if back and bw[0] not in ban and bw[0] >= 0 and bw not in v:
                    q.append(bw)
                    v.add(bw)
            j += 1
        return -1

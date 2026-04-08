class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        deg = defaultdict(int)
        for u,v in pairs:
            g[u].append(v)
            deg[u] += 1
            deg[v] -= 1
        s = pairs[0][0]
        for node, diff in deg.items():
            if diff == 1:
                s = node
                break
        stk = [s]
        arr = []
        while stk:
            while g[stk[-1]]:
                stk.append(g[stk[-1]].pop())
            arr.append(stk.pop())
        arr.reverse()
        return [[arr[i], arr[i + 1]] for i in range(len(arr) - 1)]

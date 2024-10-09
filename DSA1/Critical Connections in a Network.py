class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = [[] for i in range(n)]
        for n1, n2 in connections:
            g[n1].append(n2)
            g[n2].append(n1)
        l = [n] * n
        c = []
        def dfs(node, dt, p):
            if l[node] == n:
                l[node] = dt
                for ne in g[node]:
                    if ne != p:
                        edt = dt + 1
                        adt = dfs(ne, edt, node)
                        if adt >= edt:
                            c.append((node, ne))
                        l[node] = min(l[node], adt)
            return l[node]
        dfs(n - 1, 0, -1)
        return c            

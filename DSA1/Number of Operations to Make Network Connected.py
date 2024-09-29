class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        count = 0
        net = [i for i in range(n)]
        def find(x):
            if net[x] != x:
                net[x] = find(net[x])
            return net[x]
        def union(a, b):
            ra = find(a)
            rb = find(b)
            net[ra] = rb
            return True if ra == rb else False
        for l in connections:
            if union(l[0], l[1]):
                count += 1
        a = len(set([find(i) for i in range(n)]))
        return -1 if a - 1 > count else a - 1

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        pa = []
        s = [(0, [0])]
        while s:
            n, p = s.pop()
            if n == len(graph) - 1:
                pa.append(p)
            for n in graph[n]:
                s.append((n, p + [n]))
        return pa

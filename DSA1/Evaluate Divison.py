class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        g = defaultdict(dict)
        for i, (s, d) in enumerate(equations):
            g[s][d] = values[i]
            g[d][s] = 1 / values[i]
        
        def dfs(s, d, ans):
            if s not in g or d not in g or s in vis:
                return -1
            if s == d:
                return ans
            vis.add(s)
            for n, val in g[s].items():
                temp = dfs(n, d, ans * val)
                if temp != -1:
                    return temp
            return -1
        
        ans = []
        for s, d in queries:
            vis = set()
            val = dfs(s, d, 1)
            ans.append(val)
        return ans

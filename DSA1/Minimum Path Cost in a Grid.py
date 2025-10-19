class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[v for v in grid[i]] for i in range(n)]
        for i in range(1, n):
            for j in range(m):
                all = [dp[i - 1][k] + moveCost[grid[i - 1][k]][j] for k in range(m)]
                dp[i][j] = min(all) + grid[i][j]
        return min(dp[-1])

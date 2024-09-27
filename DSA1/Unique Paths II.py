class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * c for i in range(r)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(1, r):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]
            else:
                dp[i][0] = 0
        for i in range(1, c):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = dp[0][i - 1]
            else:
                dp[0][i] = 0
        for i in range(1, r):
            for j in range(1, c):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0
        return dp[-1][-1]

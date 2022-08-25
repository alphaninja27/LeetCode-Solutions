class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # create 2D array dp[m][n], initialize with zero
        dp = [[0 for j in range(n)] for i in range(m)]
        
        # initialize dp[0][n] with 1
        for i in range(n):
            dp[0][i] = 1
            
        # initialize dp[m][0] with 1
        for i in range(m):
            dp[i][0] = 1
            
        # assign dp[i][j] with the sum of upper cell and left cell values
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[m-1][n-1]

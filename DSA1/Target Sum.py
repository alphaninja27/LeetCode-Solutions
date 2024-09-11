class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sums = sum(nums)
        if sums < abs(target) or (sums + target) & 1:
            return 0
        def knapsack(target: int) -> int:
            dp = [1] + [0] * sums
            for n in nums:
                for i in range(sums, n - 1, -1):
                    dp[i] += dp[i - n]
            return dp[target]
        return knapsack((sums + target) // 2)

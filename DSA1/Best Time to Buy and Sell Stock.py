class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = 10000000
        y = 0
        for i in range(len(prices)):
            x = min(x, prices[i])
            y = max(y, prices[i] - x)
        return y

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy = [float("inf")] * k
        prof = [0] * k
        for p in prices:
            for i in range(k):
                buy[i] = min(buy[i], p - (prof[i - 1] if i > 0 else 0))
                prof[i] = max(prof[i], p - buy[i])
        return prof[k - 1] if k > 0 else 0

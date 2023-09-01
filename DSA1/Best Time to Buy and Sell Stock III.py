class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        A = -prices[0]
        B = float('-inf')
        C = float('-inf')
        D = float('-inf')
        for p in prices:
            A = max(A, -p)
            B = max(B, A + p)
            C = max(C, B - p)
            D = max(D, C + p)
        return D

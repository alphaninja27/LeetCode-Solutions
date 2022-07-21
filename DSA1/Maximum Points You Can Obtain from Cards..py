class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        w = len(cardPoints) - k
        total = sum(cardPoints)
        mn = s = sum(cardPoints[:w])
        for i in range(k):
            s -= cardPoints[i]
            s += cardPoints[i + w]
            mn = min(mn, s)
        return total - mn

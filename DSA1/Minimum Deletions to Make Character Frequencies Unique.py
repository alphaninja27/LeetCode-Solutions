class Solution:
    def minDeletions(self, s: str) -> int:
        count = collections.Counter(s)
        freq = set()
        d = 0
        for i, j in count.items():
            while j in freq and j > 0:
                d += 1
                j -= 1
            freq.add(j)
        return d

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        h = {}
        for n in nums:
            h[n] = h.get(n, 0) + 1
        count = 0
        for n in h:
            if k == 0:
                if h[n] > 1:
                    count += 1
            else:
                if n + k in h:
                    count += 1
        return count

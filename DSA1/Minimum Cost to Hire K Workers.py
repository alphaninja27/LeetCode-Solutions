class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        w = []
        for i in range(n):
            w.append((wage[i] / quality[i], quality[i]))
        w.sort()
        mh = []
        t = 0
        mini = float('inf')
        sums = 0
        for r, q in w:
            heapq.heappush(mh, -q)
            t += q
            sums += q
            if len(mh) > k:
                sums += heapq.heappop(mh)
            if len(mh) == k:
                mini = min(mini, sums * r)
        return mini

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        maxi = 0
        j = sorted([(s, e, p) for s, e, p in zip(startTime, endTime, profit)])
        minheap = []
        for i in range(len(startTime)):
            startTime[i] = j[i][0]
        for s,e,p in j:
            while minheap and s >= minheap[0][0]:
                maxi = max(maxi, heapq.heappop(minheap)[1])
            heapq.heappush(minheap, (e, p + maxi))
        return max(maxi, max(p for i, p in minheap))

import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events, key = lambda x:(x[0], x[1]))
        curr = 0
        heap = []
        count = 0
        i = 0
        while i < len(events) or heap:
            if not heap:
                curr = events[i][0]
            while i < len(events) and events[i][0] <= curr:
                heapq.heappush(heap, events[i][1])
                i += 1
            heapq.heappop(heap)
            count += 1
            curr += 1
            while heap and heap[0]< curr:
                heapq.heappop(heap)
        return count

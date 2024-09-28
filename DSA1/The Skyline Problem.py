class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heap = [0]
        line = []
        for l, r, h in buildings:
            line.append([l, -h])
            line.append([r, h])
        line.sort()
        ans = []
        for e, h in line:
            if h < 0:
                if h < heap[0]:
                    ans.append([e, -h])
                heapq.heappush(heap, h)
            else:
                heap.remove(-h)
                heapq.heapify(heap)
                if -h < heap[0]:
                    ans.append([e, -heap[0]])
        return ans
        

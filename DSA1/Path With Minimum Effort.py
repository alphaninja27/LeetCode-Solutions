class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dist = [[float('inf')] * n for i in range(m)]
        dist[0][0] = 0
        moves = [(0,1), (1, 0), (0, -1), (-1, 0)]
        pq = [(0, 0, 0)]
        while pq:
            w, i , j = heappop(pq)
            if (i, j) == (m - 1, n - 1):
                return w
            for k in moves:
                y, x = i + k[0], j + k[1]
                if y < 0 or y >= m or x < 0 or x >= n:
                    continue
                e = max(abs(heights[y][x] - heights[i][j]), w)
                if e < dist[y][x]:
                    dist[y][x] = e
                    heappush(pq, (dist[y][x], y, x))

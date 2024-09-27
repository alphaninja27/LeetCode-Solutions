class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for r in grid:
            if r[0] == 0:
                for j in range(len(r)):
                    if r[j] == 0:
                        r[j] = 1
                    else:
                        r[j] = 0
        l = len(grid[0])
        t = len(grid) * 2 ** (l - 1)
        i = 1
        while i < l:
            j = 0
            o = 0
            while j < len(grid):
                if grid[j][i] == 1: 
                    o += 1
                j += 1
            t += 2 ** (l - 1 - i) * max(o, len(grid) - o)
            i += 1
        return t

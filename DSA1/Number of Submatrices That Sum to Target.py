class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        x = len(matrix)
        y = len(matrix[0])
        for r in matrix:
            for i in range(y - 1):
                r[i + 1] += r[i]
        ans = 0
        for i in range(y):
            for j in range(i, y):
                c = collections.defaultdict(int)
                curr = 0
                c[0] = 1
                for k in range(x):
                    curr += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    ans += c[curr - target]
                    c[curr] += 1
        return ans

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        ans = [True] * n
        i = 2
        while (i * i) < n:
            if ans[i]:
                for j in range(i * i, n, i):
                    ans[j] = False
            i += 1
        return ans.count(True) - 2

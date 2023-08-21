class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        s = set()
        i = 1
        while len(s) < n:
            if k - i not in s:
                s.add(i)
            i += 1
        return sum(s)

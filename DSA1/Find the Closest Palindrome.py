class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        if n == 1 or n == 0:
            return str(int(n) - 1)
        p = set()
        p.add(str(10 ** (l - 1) - 1))
        p.add(str(10 ** l + 1))
        fh = int(n[:(l + 1) // 2])
        for i in [-1, 0, 1]:
            nh = str(fh + i)
            if l % 2 == 0:
                c = nh + nh[::-1]
            else:
                c = nh + nh[-2::-1]
            p.add(c)
        ni = int(n)
        cp = None
        mini = float('inf')
        for c in p:
            if c == n:
                continue
            ci = int(c)
            d = abs(ci - ni)
            if d < mini or d == mini and ci < cp:
                cp = ci
                mini = d
        return str(cp)

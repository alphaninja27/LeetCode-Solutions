from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = Counter(t)
        req = len(freq)
        n = len(s)
        l = 0
        short = n + 1
        a = -1
        b = -1
        form = 0
        for r in range(n):
            if s[r] in freq:
                freq[s[r]] -= 1
                if freq[s[r]] == 0:
                    form += 1
            while l <= r and form == req:
                if r -l + 1 < short:
                    short = r - l + 1
                    a, b = l, r
                if s[l] in freq:
                    if freq[s[l]] == 0:
                        form -= 1
                    freq[s[l]] += 1
                l += 1
        return "" if a == -1 else s[a:b + 1]

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = 'dd'
        d = {"a": a, "b": b, "c": c}
        while(True):
            e = -1
            for k, v in sorted(d.items(), key = lambda x: x[1], reverse = True):
                if not (k == ans[-1] == ans[-2]) and v >= 1:
                    e = k
                    break
            if e == -1:
                break
            ans += e
            d[e] -= 1
        return ans[2:]

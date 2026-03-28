class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        tot = n
        center = 0.0
        while center < n:
            if center.is_integer():
                l, r = int(center) - 1, int(center) + 1
            else:
                l, r = floor(center), ceil(center)
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                tot += 1
                l -= 1
                r += 1
            center += 0.5
        return tot

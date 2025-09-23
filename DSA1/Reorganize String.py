class Solution:
    def reorganizeString(self, s: str) -> str:
        a = sorted(sorted(s), key = s.count, reverse = True)
        m = len(a) // 2 if len(a) % 2 == 0 else len(a) // 2 + 1
        a[::2], a[1::2] = a[:m], a[m:]
        return ''.join(a) if len(a) == 1 or a[0] != a[1] else ""

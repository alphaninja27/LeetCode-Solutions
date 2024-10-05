class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        st, pa, mat, si = 0, 0, 0, -1
        while st< len(s):
            if pa < len(p) and (p[pa] == '?' or p[pa] == s[st]):
                st += 1
                pa += 1
            elif pa < len(p) and p[pa] == '*':
                si = pa
                mat = st
                pa += 1
            elif si != -1:
                pa = si + 1
                mat += 1
                st = mat
            else:
                return False
        while pa < len(p) and p[pa] == '*':
            pa += 1
        return pa == len(p)

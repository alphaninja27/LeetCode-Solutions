class Solution:
    def decodeString(self, s: str) -> str:
        ans, n = "", 0
        st = []
        for c in s:
            if c.isdigit():
                n = n * 10 + int(c)
            elif c == "[":
                st.append(ans)
                st.append(n)
                ans = ""
                n = 0
            elif c == "]":
                pn = st.pop()
                ps = st.pop()
                ans = ps + pn * ans
            else:
                ans += c
        return ans

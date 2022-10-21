class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        for i in s.split():
            ans = i + " " + ans
        return ans[:-1]

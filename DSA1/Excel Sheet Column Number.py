class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans, pos = 0, 0
        for l in reversed(columnTitle):
            digit = ord(l) - 64
            ans += digit * 26 ** pos
            pos += 1
        return ans

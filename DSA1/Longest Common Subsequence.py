class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        x, y = len(text1), len(text2)
        l = []
        for i in range(x + 1):
            v = [0] * (y + 1)
            l.append(v)
        for i in range(1, x + 1):
            for j in range(1, y + 1):
                if text1[i - 1] == text2[j - 1]:
                    l[i][j] = l[i - 1][j - 1] + 1
                else:
                    l[i][j] = max(l[i - 1][j], l[i][j - 1])
        return l[x][y]
        

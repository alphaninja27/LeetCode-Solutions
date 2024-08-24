class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        for i in range(0, len(s), k):
            ans.append(s[i:i + k])
        diff = abs(len(ans[-1]) - k)
        if len(ans[-1]) != k:
            for i in range(diff):
                ans[-1] += fill
        return ans

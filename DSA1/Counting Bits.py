class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        s = ""
        for i in range(n + 1):
            if i == 0:
                ans.append(0)
            else:
                s = str(bin(i)[2:])
                ans.append(s.count("1"))
        return ans

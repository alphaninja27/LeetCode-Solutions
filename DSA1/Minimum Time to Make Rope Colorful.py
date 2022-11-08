class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        pre = 0
        for i in range(1, len(colors)):
            if colors[pre] != colors[i]:
                pre = i
            else:
                res += min(neededTime[pre], neededTime[i])
                if neededTime[pre] < neededTime[i]:
                    pre = i
        return res
        

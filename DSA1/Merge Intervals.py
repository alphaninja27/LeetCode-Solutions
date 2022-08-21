class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        
        for start, end in intervals:
            prev_end = res[-1][1] if res else -1
            if start > prev_end:
                res.append([start, end])
            else:
                res[-1][1] = max(prev_end, end)
        
        return res

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        ans = []
        d = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] == x:
                count += 1
                d[count] = i
        for q in queries:
            if q > count:
                ans.append(-1)
            else:
                ans.append(d[q])
        return ans

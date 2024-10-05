class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        ans = []
        for i, n in enumerate(nums):
            for r in self.permute(nums[:i] + nums[i + 1:]):
                ans.append([n] + r)
        return ans

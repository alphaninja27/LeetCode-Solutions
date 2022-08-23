class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(sorted(set(nums)))
        ans = []
        count = 1
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                count += 1
            else:
                ans.append(count)
                count = 1
            ans.append(count)
        return max(ans)

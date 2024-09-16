class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            if nums[i] < ans[-1]:
                for j in ans:
                    if j >= nums[i]:
                        ans[ans.index(j)] = nums[i]
                        break
        return len(ans)

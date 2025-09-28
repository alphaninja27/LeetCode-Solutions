class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort = sorted(nums)
        i,j = -1, -1
        for i in range(len(nums)):
            if sort[i] != nums[i]:
                break
        for j in range(len(nums) - 1, -1, -1):
            if sort[j] != nums[j]:
                break
        if i < j:
            return j - i + 1
        return 0

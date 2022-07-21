class Solution:
    def canJump(self, nums: List[int]) -> bool:
        first = 0
        last = len(nums) - 1
        for i in range(len(nums)):
            if i > first:
                return False
            if nums[i] + i > first:
                first = nums[i] + i
            if first >= last:
                return True

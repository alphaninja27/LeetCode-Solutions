class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        l=len(nums)
        nums.sort()
        return max(nums[l-1]*nums[l-2]*nums[l-3], nums[l-1]*nums[0]*nums[1])

class Solution:
    def rob(self, nums: List[int]) -> int:
        def help(nums):
            r1, r2 = 0, 0
            for i in nums:
                temp = max(i + r1, r2)
                r1 = r2
                r2 = temp
            return r2
        return max(help(nums[1:]), help(nums[:-1]), nums[0])

class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        z, z1, z12 = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                z = 2 * z + 1
            elif nums[i] == 1:
                z1 = 2 * z1 + z
            else:
                z12 = 2 * z12 + z1
        return z12 % (10 ** 9 + 7)

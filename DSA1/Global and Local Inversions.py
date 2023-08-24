class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        maxi = -1
        for i in range(1, len(nums)):
            if nums[i] < maxi:
                return False
            maxi = max(maxi, nums[i - 1])
        return True

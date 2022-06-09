class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x=0
        nums.sort()
        l=len(nums)
        for i in range(0,l+1):
            if i not in nums:
                x=i
        return x

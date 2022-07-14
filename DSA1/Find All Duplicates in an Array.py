class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            i = abs(i)
            if nums[i - 1] > 0:
                nums[i - 1] *= -1
            else:
                ans.append(i)
        return ans

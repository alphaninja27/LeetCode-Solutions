class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans = []
        while nums:
            a = min(nums)
            nums.remove(min(nums))
            b = min(nums)
            nums.remove(min(nums))
            ans.append(b)
            ans.append(a)
        return ans

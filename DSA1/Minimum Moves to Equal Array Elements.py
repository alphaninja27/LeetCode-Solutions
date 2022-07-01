class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        mini = min(nums)
        for i in nums:
            count += i - mini
        return count

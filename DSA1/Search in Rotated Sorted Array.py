class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            p = nums[m]
            if p == target:
                return m
            if nums[l] <= p:
                if target > p or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < p or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
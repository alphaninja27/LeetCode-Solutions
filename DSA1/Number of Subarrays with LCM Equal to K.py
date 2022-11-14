import math
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            l = nums[i]
            for j in range(i, len(nums)):
                l = math.lcm(l, nums[j])
                if l == k:
                    count += 1
                elif l > k:
                    break
        return count

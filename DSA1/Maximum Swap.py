class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        last = {int(d): i for i, d in enumerate(nums)}
        for i, dig in enumerate(nums):
            for d in range(9, int(dig), -1):
                if last.get(d, -1) > i:
                    nums[i], nums[last[d]] = nums[last[d]], nums[i]
                    return int(''.join(nums))
        return num

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = [0] * k
        sums = 0
        for i in nums:
            sums += i % k
            count[sums % k] += 1
        ans = count[0]
        for i in count:
            ans += (i*(i-1)) // 2
        return ans

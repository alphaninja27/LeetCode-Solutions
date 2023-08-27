class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0 : 1}
        count = 0
        sums = 0
        for n in nums:
            sums += n
            dif = sums - k
            if dif in d:
                count += d[dif]
            if sums in d:
                d[sums] += 1
            else:
                d[sums] = 1
        return count

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicti = {}
        n = len (nums)
        for i in nums:
            dicti[i] = dicti.get(i, 0) + 1
        for k,v in dicti.items():
            if v > n//2:
                return k

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = []
        dicti = {}
        n = len(nums)
        for i in nums:
            dicti[i] = dicti.get(i, 0) + 1
        for k,v in dicti.items():
            if v > n//3:
                ans.append(k)
        return ans
        

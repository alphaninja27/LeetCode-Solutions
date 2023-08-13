class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr, ans = sorted(nums), []
        for n in nums:
            i = bisect_left(arr, n)
            ans.append(i)
            del arr[i]
        return ans

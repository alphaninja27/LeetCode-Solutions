class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = []
        nums4 = []
        for i in range(m):
            nums3.append(nums1[i])
        for i in range(n):
            nums4.append(nums2[i])
        ans = nums3 + nums4
        nums1.clear()
        for i in ans:
            nums1.append(i)
        nums1.sort()

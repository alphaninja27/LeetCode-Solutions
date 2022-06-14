class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = {}
        stack = []
        for i in nums2:
            while len(stack) > 0 and i > stack[-1]:
                greater[stack.pop()] = i
            stack.append(i)
        
        ans = []
        for i in nums1:
            if i in greater:
                ans.append(greater[i])
            else:
                ans.append(-1)
        return ans

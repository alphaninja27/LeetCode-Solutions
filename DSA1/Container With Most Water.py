class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        maxi = 0
        while start < end:
            maxi = max(maxi, min(height[start], height[end]) * (end - start))
            if height[start] >= height[end]:
                end -= 1
            else:
                start += 1
        return maxi

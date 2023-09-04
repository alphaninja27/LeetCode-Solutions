class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        w = 0
        while l < r:
            lmax, rmax = max(lmax, height[l]), max(rmax, height[r])
            if lmax <= rmax:
                w += lmax - height[l]
                l += 1
            else:
                w += rmax - height[r]
                r -= 1
        return w

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def finish(k):
            hours = 0
            for p in piles:
                hours += p // k
                if p % k != 0:
                    hours += 1
                if hours > h:
                    return False
            return True
        l, r = 1, max(piles)
        ans = r
        while l <= r:
            mid = l + (r - l) // 2
            if finish(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

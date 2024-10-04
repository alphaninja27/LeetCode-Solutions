class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = [1] * len(ratings)
        for l in range(1, len(ratings)):
            if ratings[l - 1] < ratings[l]:
                ans[l] = ans[l - 1] + 1
        for r in range(len(ratings) - 2, -1, -1):
            if ratings[r + 1] < ratings[r]:
                ans[r] = max(ans[r], ans[r + 1] + 1)
        return sum(ans)

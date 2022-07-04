class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        x = 1
        y = 2
        for i in range(3,n):
            temp = y
            y += x
            x = temp
        return x + y

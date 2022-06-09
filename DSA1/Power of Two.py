class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x=0
        for i in range(0,1000):
            if pow(2,i)==n:
                x=1
        if x:
            return True
        else:
            return False

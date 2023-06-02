class Solution:
    def getSum(self, a: int, b: int) -> int:
        bitShortener = 0xffffffff
        while (b & bitShortener) > 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry
        return (a & bitShortener) if b > 0 else a

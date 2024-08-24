class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        x ,y = len(num1) - 1, len(num2) - 1
        ans = []
        carry = 0
        while x >= 0 or y >= 0 or carry:
            a = int(num1[x]) if x >= 0 else 0
            b = int(num2[y]) if y >= 0 else 0
            tot = a + b + carry
            carry = tot // 10
            ans.append(str(tot%10))
            x -= 1
            y -= 1
        return "".join(ans[::-1])

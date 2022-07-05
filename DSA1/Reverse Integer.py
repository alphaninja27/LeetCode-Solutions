class Solution:
    def reverse(self, x: int) -> int:
        temp = str(x)
        if x < 0:
            temp = temp[1:]
            
        temp = int(temp[::-1])
        
        if temp >= (2**31) - 1: return 0
        elif x < 0: return "-" + str(temp)
        else: return temp

class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        for i in s:
            if not stk:
                stk.append(i)
            else:
                if i.islower() and i.upper() == stk[-1]:
                    stk.pop()
                    continue
                elif i.isupper() and i.lower() == stk[-1]:
                    stk.pop()
                    continue
                stk.append(i)
        return ''.join(stk)
        

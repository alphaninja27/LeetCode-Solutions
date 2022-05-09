class Solution:
    def isHappy(self, n: int) -> bool:
        def sq(num):
            res=0
            while num>0:
                r=num%10
                res=res+r*r
                num=num//10
            return res
        
        seen=set()
        
        while sq(n) not in seen:
            s1=sq(n)
            if s1==1:
                return True
            else:
                seen.add(s1)
                n=s1
        return False

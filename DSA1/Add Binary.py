class Solution:
    def addBinary(self, a: str, b: str) -> str:
        r=""
        c=0
        a,b=a[::-1],b[::-1]
        for i in range(max(len(a),len(b))):
            da=int(a[i]) if i<len(a) else 0
            db=int(b[i]) if i<len(b) else 0
            total=da+db+c
            char=str(total%2)
            r=char+r
            c=total//2
            
        if c:
            r="1"+r
        return r

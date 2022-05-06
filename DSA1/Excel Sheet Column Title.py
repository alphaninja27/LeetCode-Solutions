class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        r=""
        while(columnNumber!=0):
            columnNumber-=1
            temp=columnNumber%26
            r+=chr(65+temp)
            columnNumber=columnNumber//26
        return r[::-1]

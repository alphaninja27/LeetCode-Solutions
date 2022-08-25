class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start,end, res = 0,0,0
        while(end<len(s)):
            if(s[end] in s[start:end]):
                start+=1 
            else: 
                res = max(res, end-start+1)
                end+=1 
        return res

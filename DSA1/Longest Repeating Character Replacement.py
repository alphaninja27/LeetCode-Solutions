class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        start = 0
        end = 0
        l = 0
        counts = 0
        while end < len(s):
            count[ord(s[end]) - ord('A')] += 1
            counts = max(counts, count[ord(s[end]) - ord('A')])
            
            while end - start - counts + 1 > k:
                count[ord(s[start]) - ord('A')] -= 1
                start += 1
                
            l = max(l, end - start + 1)
            end += 1
        return l

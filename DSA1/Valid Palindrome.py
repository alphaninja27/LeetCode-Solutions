class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s.lower():
            if not i.isalnum():
                s = s.replace(i,"")
        return s.lower() == s.lower()[::-1]

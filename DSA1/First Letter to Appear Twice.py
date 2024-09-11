class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ans = set()
        for char in s:
            if char in ans:
                return char
            else:
                ans.add(char)
        

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = '0123456789'
        for i in range(len(word)):
            if word[i] not in nums:
                word = word.replace(word[i],' ')
        nl = word.split()
        ans = []
        for i in range(len(nl)):
            ans.append(int(nl[i]))
        return len(set(ans))

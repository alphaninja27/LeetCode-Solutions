class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = "!?',:;."
        for i in s:
            paragraph = paragraph.replace(i, " ")
        hm = defaultdict(int)
        paragraph = paragraph.lower()
        l1 = paragraph.split()
        for i in l1:
            if i not in banned:
                hm[i] = hm[i] + 1
        maxi = max(hm.values())
        for k, v in hm.items():
            if v == maxi:
                return k

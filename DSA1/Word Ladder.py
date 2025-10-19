class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        bset = {beginWord}
        eset = {endWord}
        vis = set()
        s = 1
        while bset and eset:
            if len(bset) > len(eset):
                bset, eset = eset, bset
            nset = set()
            for w in bset:
                for i in range(len(w)):
                    for c in string.ascii_lowercase:
                        if c == w[i]:
                            continue
                        nw = w[:i] + c + w[i + 1:]
                        if nw in eset:
                            return s + 1
                        if nw in wordSet and nw not in vis:
                            vis.add(nw)
                            nset.add(nw)
            bset = nset
            s += 1
        return 0

                
        
        

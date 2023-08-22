class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ro, co = len(board), len(board[0])
        vis = set()
        
        def dfs(r, c, ind):
            if ind == len(word):
                return True
            if r < 0 or r >= ro or c < 0 or c >= co or word[ind] != board[r][c] or (r,c) in vis:
                return False
            vis.add((r,c))
            res = (dfs(r + 1, c, ind + 1) or dfs(r - 1, c, ind + 1) or dfs(r, c + 1, ind + 1) or dfs(r, c - 1, ind + 1))
            vis.remove((r, c))
            return res
        for i in range(ro):
            for j in range(co):
                if dfs(i, j, 0):
                    return True
        return False

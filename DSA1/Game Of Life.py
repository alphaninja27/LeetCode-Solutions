class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        temp = [[None] * n for _ in range(m)]
        
        def help(r, c):
            p = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            count = 0
            for x, y in p:
                if 0 <= r + y < m and 0 <= c + x < n and board[r + y][c + x] == 1:
                    count += 1
            if board[r][c] == 1:
                if count < 2:
                    return 0
                elif count ==2 or count == 3:
                    return 1
                else:
                    return 0
            else:
                if count == 3:
                    return 1
                else:
                    return 0
        for r in range(m):
            for c in range(n):
                temp[r][c] = help(r, c)
        
        for r in range(m):
            for c in range(n):
                board[r][c] = temp[r][c]

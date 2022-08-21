r, c = len(matrix), len(matrix[0])
        
        for i in range(r):
            for j in range(c - i):
                matrix[i][j], matrix[r - j - 1][r - i - 1] = matrix[r - j - 1][r - i - 1], matrix[i][j]
        
        matrix.reverse()

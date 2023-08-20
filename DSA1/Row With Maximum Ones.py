class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        maxi = 0
        ans = 0
        for i in range(n):
            curr = 0
            for j in range(m):
                if mat[i][j] == 1:
                    curr += 1
            if curr > maxi:
                ans = i
                maxi = curr
        return [ans, maxi]

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = {}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i + j not in d:
                    d[i + j] = [mat[i][j]]
                else:
                    d[i + j].append(mat[i][j])
        ans = []
        for e in d.items():
            if e[0] % 2 == 0:
                [ans.append(x) for x in e[1][::-1]]
            else:
                [ans.append(x) for x in e[1]]
        return ans

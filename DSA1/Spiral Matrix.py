class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if not matrix:
            return ans
        x, y = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, x - 1, 0, y - 1
        dir = 0
        while top <= bottom and left <= right:
            if dir == 0:
                for i in range(left, right + 1):
                    ans.append(matrix[top][i])
                top += 1
            elif dir == 1:
                for i in range(top, bottom + 1):
                    ans.append(matrix[i][right])
                right -= 1
            elif dir == 2:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            else:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
            dir = (dir + 1) % 4
        return ans
            
        

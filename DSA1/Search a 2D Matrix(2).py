class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        r, c = len(matrix), len(matrix[0])
        s, e = 0, (r * c) - 1
        while s <= e:
            m = (s + e) // 2
            mv = matrix[m //c][m % c]
            if mv == target:
                return True
            elif mv < target:
                s = m + 1
            else:
                e = m - 1
        return False

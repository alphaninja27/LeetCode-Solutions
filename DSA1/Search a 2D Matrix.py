class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = False
        for i in matrix:
            for j in i:
                if j == target:
                    x = True
        return x
      
      
right,left=0,0
        for item in matrix:
                 if item[-1] >= target:
                                right=len(item)-1
                                while left<=right:
                                        mid=left+(right-left)//2
                                        if item[mid] == target:
                                                return True
                                        elif item[mid] < target:
                                                left=mid+1
                                        else:
                                                right=mid-1

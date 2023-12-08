from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x=0
        y=len(matrix[0])-1
        while y>=0 and x<len(matrix):
            if matrix[x][y]==target:
                return True
            elif matrix[x][y]>target:
                y-=1
            else:
                x+=1
        return False
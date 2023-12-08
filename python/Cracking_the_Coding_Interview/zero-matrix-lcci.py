from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=set()
        col=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
        for r in row:
            matrix[i]=[0]*len(matrix[0])
        for c in col:
            for i in range(len(matrix)):
                matrix[i][c]=0
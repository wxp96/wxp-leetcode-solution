from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums=[[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.sums[i+1][j+1]=self.sums[i][j+1]+self.sums[i+1][j]-self.sums[i][j]+matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2+1][col2+1]-self.sums[row2+1][col1]-self.sums[row1][col2+1]+self.sums[row1][col1]

obj = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
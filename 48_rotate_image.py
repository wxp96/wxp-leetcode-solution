from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix=list(zip(*matrix))
        col=len(matrix[0])
        for i in range(len(matrix)):
            matrix[i]=list(matrix[i])
            for j in range(len(matrix[0])//2):
                matrix[i][j],matrix[i][col-1-j]=matrix[i][col-1-j],matrix[i][j]


s=Solution()
matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(matrix)
print(matrix)
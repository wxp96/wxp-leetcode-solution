from typing import List
import copy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # tmp=copy.deepcopy(matrix)
        # n=len(matrix)
        # for i in range(n):
        #     for j in range(n):
        #         tmp[i][j]=matrix[n-j-1][i]
        # for i in range(n):
        #     for j in range(n):
        #         matrix[i][j]=tmp[i][j]
        n=len(matrix)
        for i in range(n//2):
            matrix[i],matrix[n-i-1]=matrix[n-i-1],matrix[i]
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
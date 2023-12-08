from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp_1=[0]*len(matrix[0])
        dp_2=[0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='1':
                    if i==0 or j==0:
                        dp_2[j]=1
                    else:
                        dp_2[j]=min(dp_1[j],dp_1[j-1],dp_2[j-1])+1
            max_side=max(dp_2)
            dp_1=dp_2

        return max_side**2

s=Solution()
print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
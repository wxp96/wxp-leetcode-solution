from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo=[float('inf')]*len(grid[0])
        memo[0]=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j==0:
                    memo[j]+=grid[i][j]
                else:
                    memo[j]=min(memo[j],memo[j-1])+grid[i][j]
        return memo[-1]
from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        def backtrack(i,j):
            grid[i][j]=0
            for dx,dy in movement:
                new_i,new_j=i+dx,j+dy
                if 0<=new_i<len(grid) and 0<=new_j<len(grid[0]) and grid[new_i][new_j]==1:
                    backtrack(new_i,new_j)

        movement=((-1,0),(0,-1),(1,0),(0,1))
        for i in range(len(grid)):
            if grid[i][0]==1:
                backtrack(i,0)
            if grid[i][len(grid[0])-1]==1:
                backtrack(i,len(grid[0])-1)

        for j in range(len(grid[0])):
            if grid[0][j]==1:
                backtrack(0,j)
            if grid[len(grid)-1][j]==1:
                backtrack(len(grid)-1,j)

        return sum([sum(grid[i]) for i in range(len(grid))])
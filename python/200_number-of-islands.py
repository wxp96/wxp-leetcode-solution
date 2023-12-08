from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i,j):
            grid[i][j]="-1"
            for di,dj in movement:
                new_i,new_j=i+di,j+dj
                if 0<=new_i<len(grid) and 0<=new_j<len(grid[0]) and grid[new_i][new_j]=="1":
                    dfs(new_i,new_j)

        res=0
        movement=((-1,0),(1,0),(0,-1),(0,1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    dfs(i,j)
                    res+=1
        return res
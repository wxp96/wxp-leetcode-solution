from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(i,j):
            nonlocal area
            grid[i][j]=-1
            area+=1
            for di,dj in movement:
                new_i,new_j=i+di,j+dj
                if 0<=new_i<len(grid) and 0<=new_j<len(grid[0]) and grid[new_i][new_j]==1:
                    dfs(new_i,new_j)


        res=0
        movement=((-1,0),(1,0),(0,-1),(0,1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    area=0
                    dfs(i,j)
                    res=max(res,area)
        return res
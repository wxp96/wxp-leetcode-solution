from typing import List
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def backtrack(i,j):
            grid[i][j]=-1
            res=True
            if i==0 or j==0 or i==len(grid)-1 or j==len(grid[0])-1:
                res=False
            for di,dj in movement:
                new_i,new_j=i+di,j+dj
                if 0<=new_i<len(grid) and 0<=new_j<len(grid[0]) and grid[new_i][new_j]==0:
                    next=backtrack(new_i,new_j)
                    res=res and next
            return res

        movement=((-1,0),(1,0),(0,-1),(0,1))
        ans=0
        for i in range(1,len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0 and backtrack(i,j):
                    ans+=1
        return ans

s=Solution()
print(s.closedIsland([
    [1,1,0,1,1,1,1,1,1,1],
    [0,0,1,0,0,1,0,1,1,1],
    [1,0,1,0,0,0,1,0,1,0],
    [1,1,1,1,1,0,0,1,0,0]]))
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def backtrack(x,y):
            grid[x][y]='0'
            for i,j in movement:
                if x+i<len(grid) and x+i>=0 and y+j>=0 and y+j<len(grid[0]) and grid[x+i][y+j]=='1':
                    backtrack(x+i,y+j) 

        movement=[(0,1),(1,0),(-1,0),(0,-1)]
        cnt=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    cnt+=1
                    backtrack(i,j)
        return cnt
    
s=Solution()
print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        def backward(i,j):
            ans=True
            if i==0 or i==len(grid)-1 or j==0 or j== len(grid[0])-1:
                ans=False
            grid[i][j]=2
            cnt=1
            for x,y in ((1,0),(0,1),(-1,0),(0,-1)):
                if 0<=i+x<len(grid) and 0<=y+j<len(grid[0]) and grid[i+x][j+y]==1:
                    res=backward(i+x,j+y)
                    ans= ans and res[0]
                    cnt=cnt+res[1]
            return ans,cnt

        rs=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    tmp=backward(i,j)
                    if tmp[0]:
                        rs+=tmp[1]
        return rs

s=Solution()
print(s.numEnclaves([[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]))
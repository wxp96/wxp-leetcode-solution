from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res=[[0]*n for i in range(n)]
        dxy=[(0,1),(1,0),(0,-1),(-1,0)]
        j=0
        dx,dy=dxy[j]
        x,y=0,0
        for i in range(n**2):
            res[x][y]=i+1
            if x+dx>=n or x+dx<=-1 or y+dy>=n or y+dy<=-1 or res[x+dx][y+dy]!=0:
                j=(j+1)%4
                dx,dy=dxy[j]
            x+=dx
            y+=dy
        return res
from typing import List
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans=[]
        for i in range(len(grid[0])):
            now_row=0
            now_col=i
            while now_row<len(grid):
                board_i=grid[now_row][now_col]
                if now_col == 0 and board_i==-1 or now_col==len(grid[0])-1 and board_i==1:
                    now_col=-1
                    break
                elif board_i!=grid[now_row][now_col+board_i]:
                    now_col=-1
                    break
                else:
                    now_col+=board_i
                    now_row+=1
            ans.append(now_col)
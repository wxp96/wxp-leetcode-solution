from pickle import FALSE
from typing import List
from collections import defaultdict
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i,j):
            visited.add((i,j))
            for dx,dy in dxy:
                if 0<=i+dx<len(board) and 0<=j+dy<len(board[0]) and board[i+dx][j+dy]=="O" and (i+dx,j+dy) not in visited:
                    dfs(i+dx,j+dy)
                

        dxy=((-1,0),(0,-1),(1,0),(0,1))
        visited=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="O" and (i==0 or i==len(board)-1 or j==0 or j==len(board[0])-1):
                    dfs(i,j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in visited and board[i][j]=='O':
                    board[i][j]='X'

s=Solution()
print(s.solve([["X","O","X","O","X","O","O","O","X","O"],["X","O","O","X","X","X","O","O","O","X"],["O","O","O","O","O","O","O","O","X","X"],["O","O","O","O","O","O","X","O","O","X"],["O","O","X","X","O","X","X","O","O","O"],["X","O","O","X","X","X","O","X","X","O"],["X","O","X","O","O","X","X","O","X","O"],["X","X","O","X","X","O","X","O","O","X"],["O","O","O","O","X","O","X","O","X","O"],["X","X","O","X","X","X","X","O","O","O"]]))
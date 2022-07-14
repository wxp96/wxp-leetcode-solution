from typing import List
from copy import deepcopy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def qualified(j):
            # test row qualified
            diag=j-q[j]
            diag_r=j+q[j]
            for i in range(j):
                if q[i]==q[j] or i-q[i]==diag or i+q[i]==diag_r:
                    return False
            return True


        def dfs(i):
            if not qualified(i-1):
                return
            if i==n:
                res.append([''.join(row) for row in temp])
                return
            for j in range(n):
                q[i]=j
                temp[i][j]='Q'
                dfs(i+1)
                q[i]=-1
                temp[i][j]='.'

        res=[]
        q=[-1]*n
        temp=[['.']*n for i in range(n)]
        dfs(0)
        return res

s=Solution()
print(s.solveNQueens(4))
from typing import List
from functools import lru_cache
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l=r=n
        @lru_cache()
        def dfs(l,r):
            res=[]
            if l==0:
                if r==0:
                    return []
                else:
                    return [')'*r]
            if r==0 and l!=0:
                return []
            if l==r:
                for k in dfs(l-1,r):
                    res.append('('+k)
            elif l<r:
                for k in dfs(l-1,r):
                    res.append('('+k)
                for k in dfs(l,r-1):
                    res.append(')'+k)
            elif l>r:
                return []
            return res
        return dfs(n,n)

s=Solution()
print(s.generateParenthesis(3))

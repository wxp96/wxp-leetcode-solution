from typing import List
from collections import deque
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        lremove=rremove=0
        for c in s:
            if c=='(':
                lremove+=1
            elif c==')':
                if lremove==0:
                    rremove+=1
                else:
                    lremove-=1

        def is_valid(s):
            dq=deque()
            for c in s:
                if c=="(":
                    dq.append(c)
                elif c==')':
                    if dq:
                        dq.pop()
                    else:
                        return False
            return True if not dq else False
        
        def backtrack(s,pos,l,r):
            if l==r==0 and is_valid(s):
                res.add(s)
                return
            for i in range(pos,len(s)):
                if i>=1 and s[i]==s[i-1]:
                    continue
                if s[i]=='(' and l>0:
                    backtrack(s[:i]+s[i+1:],i,l-1,r)
                elif s[i]==')' and r>0:
                    backtrack(s[:i]+s[i+1:],i,l,r-1)

        res=set()
        backtrack(s,0,lremove,rremove)
        return list(res)
    
s=Solution()
s.removeInvalidParentheses('(')
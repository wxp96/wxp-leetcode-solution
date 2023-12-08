from collections import deque
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dq1=deque()
        dq2=deque()
        dq2.append(-1)
        for i,cha in enumerate(s):
            if dq1 and cha==')' and dq1[-1]=='(':
                dq1.pop()
                dq2.pop()
            else:
                dq1.append(cha)
                dq2.append(i)
        dq2.append(len(s))
        result=0
        for j in range(len(dq2)-1,0,-1):
            result=max(result,dq2[j]-dq2[j-1]-1)
        return result

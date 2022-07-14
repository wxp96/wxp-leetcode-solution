class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def dp(i,j):
            if i==len(s) and j==len(p):
                return True
            if j==len(p):
                return False
            if (i,j) in memo.keys():
                return memo[(i,j)]
            if i<len(s) and (s[i]==p[j] or p[j]=='.'):
                if len(p)-j>1 and p[j+1]=='*':
                    memo[(i,j)]=dp(i+1,j) or dp(i+1,j+2) or dp(i,j+2)
                else:
                    memo[(i,j)]=dp(i+1,j+1)
            else:
                if len(p)-j>1 and p[j+1]=='*':
                    memo[(i,j)]=dp(i,j+2)
                else:
                    memo[(i,j)]=False
            return memo[(i,j)]

        memo=dict()
        return dp(0,0)

s=Solution()
print(s.isMatch("aaab","a*a*c"))
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp1=[False]*(len(p)+1)
        dp1[0]=True
        for i in range(len(p)):
            if p[i]=='*':
                dp1[i+1]=dp1[i-1]
        for i in range(len(s)):
            dp2=[False]*(len(p)+1)
            for j in range(len(p)):
                if s[i]==p[j] or p[j]=='.':
                    dp2[j+1]=dp1[j]
                elif p[j]=='*':
                    if s[i]==p[j-1] or p[j-1]=='.':
                        dp2[j+1]=dp1[j-1] or dp2[j-1] or dp1[j+1]
                    else:
                        dp2[j+1]=dp2[j-1]
            dp1=dp2
        return dp1[-1]

s=Solution()
print(s.isMatch('aab','c*a*b'))
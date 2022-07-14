
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s_r=list(reversed(s))
        m=len(s)
        memo=[0]*(m+1)
        for i in range(1,m+1):
            memo1=[0]*(m+1)
            for j in range(1,m+1):
                if s[i-1]==s_r[j-1]:
                    memo1[j]=memo[j-1]+1
                else:
                    memo1[j]=max(memo[j],memo1[j-1])
            memo=memo1
        return memo[-1]

s=Solution()
print(s.longestPalindromeSubseq("bbbab"))
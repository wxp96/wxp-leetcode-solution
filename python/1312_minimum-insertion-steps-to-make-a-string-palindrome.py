class Solution:
    def minInsertions(self, s: str) -> int:
        memo=[0]*(len(s)+1)
        for i in range(1,len(s)+1):
            pre=0
            for j in range(len(s),0,-1):
                idx=len(s)-j+1
                cur=memo[idx]
                if s[i-1]==s[j-1]:
                    memo[idx]=pre+1
                else:
                    memo[idx]=max(memo[idx],memo[idx-1])
                pre=cur
        return len(s)-memo[-1]

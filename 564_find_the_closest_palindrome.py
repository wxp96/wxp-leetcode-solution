class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l_n=list(str(n))
        l_n1=list(str(n))
        if len(l_n)>1:
            mid=(len(l_n)+1)//2
            for i in range(0,mid):
                l_n[i]=l_n[-1-i]
                n_s=''.join(l_n)
            mid=len(l_n)//2+1
            for j in range(mid,len(l_n)):
                l_n1[i]=l_n1[-1-i]
                n_s1=''.join(l_n1)
            if n_s1==n_s:
                return str(int(n_s)-1)
            else:
                return min(n_s,n_s1)
        else:
            return str(n-1)

s=Solution()
print(s.nearestPalindromic)
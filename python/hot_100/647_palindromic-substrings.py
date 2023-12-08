class Solution:
    def countSubstrings(self, s: str) -> int:
        new_s='$#'
        for cha in s:
            new_s+=cha
            new_s+='#'
        new_s+='!'
        f=[0]*len(new_s)
        max_i=max_r=ans=0
        for i in range(1,len(new_s)-1):
            f[i]=min(max_r-i+1,f[2*max_i-i]) if i<=max_r else 1
            while new_s[i+f[i]]==new_s[i-f[i]]:
                f[i]+=1
            if i+f[i]-1>max_r:
                max_i=i
                max_r=i+f[i]-1
            ans+=f[i]//2
        return ans

s=Solution()
print(s.countSubstrings('abc'))
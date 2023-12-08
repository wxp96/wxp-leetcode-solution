from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        l=0
        r=1
        d=dict()
        res=1
        d[s[l]]=0
        while r<len(s):
            while r<len(s) and s[r] not in d.keys():
                d[s[r]]=r
                r+=1
            res=max(res,r-d[s[l]])
            while l<r and r<len(s) and s[l]!=s[r]:
                del d[s[l]]
                l+=1
            del d[s[l]]
            l+=1
        return res
        
s=Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
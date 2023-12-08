from typing import List
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p=Counter(p)
        cnt_s=Counter()
        l=0
        res=[]
        for r in range(len(s)):
            cnt_s[s[r]]+=1
            while cnt_s[s[r]]>cnt_p[s[r]]:
                cnt_s[s[l]]-=1
                l+=1
            if r-l+1==len(p):
                res.append(l)
        return res

 
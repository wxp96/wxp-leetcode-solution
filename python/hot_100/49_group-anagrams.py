from typing import List
from functools import reduce
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def inner(s):
            tmp=[0]*26
            for chr in s:
                tmp[ord(chr)-ord('a')]+=1
            return tuple(tmp)

        ans=[]
        dd=defaultdict(list)
        for s in strs:
            k=inner(s)
            dd[k].append(s)
        for k in dd:
            ans.append(dd[k])
        return ans

s=Solution()
print(s.groupAnagrams(["bdddddddddd","bbbbbbbbbbc"]))

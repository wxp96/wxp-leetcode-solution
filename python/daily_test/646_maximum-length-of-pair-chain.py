from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        res=1
        pairs=sorted(pairs,key=lambda x:(x[1],x[0]))
        pre_l,pre_r=pairs[0]
        for l,r in pairs[1:]:
            if l<=pre_r:
                continue
            else:
                pre_l,pre_r=l,r
                res+=1
        return res
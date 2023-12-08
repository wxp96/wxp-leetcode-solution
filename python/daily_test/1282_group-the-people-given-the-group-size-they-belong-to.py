from typing import List
from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d=defaultdict(list)
        res=[]
        for i,g in enumerate(groupSizes):
            d[g].append(i)
        for k,v in d.items():
            tmp=[]
            for idx in v:
                if len(tmp)==k:
                    res.append(tmp)
                    tmp=[]
                tmp.append(idx)
            res.append(tmp)
        return res
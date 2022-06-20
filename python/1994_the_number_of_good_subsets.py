from typing import List
from collections import defaultdict
class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        prime=set([2,3,5,7,11,13,17,19,23,29])
        d1=defaultdict(list)
        d2=defaultdict(list)
        for i in range(2,31):
            if i in prime:
                d1[i].append(i)
                d2[i].append(i)
                continue
            for num in prime:
                if i%num==0:
                    d2[i].append(d2[i//num])
                    if len(set(d2[i]))==len(d2[i]):
                        for divid in d2[i]:
                            d1[divid].append(d2[i])
                    break
        for 

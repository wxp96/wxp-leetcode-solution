from typing import List
from collections import defaultdict
import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dd=defaultdict(list)
        start_end=tuple(zip(startTime,endTime))
        for i,(s,e) in enumerate(start_end):
            dd[(s,e)].append(profit[i])
        start_end=sorted(start_end,key=lambda x:x[1])
        for i,(s,e) in enumerate(start_end):
            profit[i]=dd[(s,e)].pop()
        memo=[0]
        keys=[0]
        for i,(s,e) in enumerate(start_end):
            idx=bisect.bisect_right(keys,s)-1
            if e!=keys[-1]:
                memo.append(max(memo[idx]+profit[i],memo[-1]))
                keys.append(e)
            else:
                memo[-1]=max(memo[idx]+profit[i],memo[-1])
        return memo[-1]

s=Solution()
print(s.jobScheduling([4,2,4,8,2],[5,5,5,10,8],[1,2,8,10,4]))
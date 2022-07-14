from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals,key=lambda x:x[1])
        pre_s,pre_e=intervals[0]
        res=0
        for start,end in intervals[1:]:
            if start<pre_e:
                res+=1
            else:
                pre_s,pre_e=start,end
        return res

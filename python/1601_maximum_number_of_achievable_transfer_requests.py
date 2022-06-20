from typing import List
from collections import defaultdict
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        def max_cycle(now):
            if not out_order[now]:
                return False,0,""
            rs_bool=False
            rs_max=0
            rs_str=""
            for i in out_order[now]:
                back=max_cycle(i)
                if back[0] and rs_max<back[1]+1:
                    rs_bool=True
                    rs_max=back[1]+1
                    rs_str=back[2]+str(now)
            for in_,out_ in list(zip(rs_str,rs_str[1:])):
                out_order[out_].remove(in_)
            return rs_bool,rs_max,rs_str

        out_order=defaultdict(list)
        # out_order_cnt=defaultdict(int)
        for x,y in requests:
            out_order[x].append(y)
        
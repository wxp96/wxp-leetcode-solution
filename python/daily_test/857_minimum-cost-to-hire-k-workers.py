from typing import List
import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        tmp=sorted(zip(quality,wage),key=lambda p:p[1]/p[0])
        totalq=0
        hq_q=[]
        res=float('inf')
        for q,w in tmp[:k-1]:
            totalq+=q
            heapq.heappush(hq_q,-q)
        for q,w in tmp[k-1:]:
            totalq+=q
            totalc=totalq*w/q
            heapq.heappush(hq_q,-q)
            res=min(res,totalc)
            totalq+=heapq.heappop(hq_q)
        return res


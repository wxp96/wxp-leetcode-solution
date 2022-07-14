from typing import List
import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pre,res,hq=0,0,[]
        remain_fuel=startFuel
        stations+=[[target,0]]
        for i,(mile,fuel) in enumerate(stations):
            remain_fuel-=mile-pre
            while remain_fuel<0 and hq:
                remain_fuel-=heapq.heappop(hq)
                res+=1
            if not hq and remain_fuel<0:
                return -1
            if i!=len(stations)-1:
                pre=mile
                heapq.heappush(hq,-fuel)
        return res

            

s=Solution()
print(s.minRefuelStops(100,50,[[25,50],[50,25]]))
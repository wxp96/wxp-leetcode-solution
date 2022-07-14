from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas=[gas[i]-cost[i] for i in range(len(gas))]
        min_i=sum=0
        min_sum=float('inf')
        for i,a in enumerate(gas):
            sum+=a
            if sum<min_sum:
                min_sum=sum
                min_i=i
        if sum<0:
            return -1
        return (min_i+1)%len(gas)

s=Solution()
s.canCompleteCircuit([11,4,7,1,0],[2,5,5,9,1])
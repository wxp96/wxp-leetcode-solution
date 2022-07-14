from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo=[[-float('inf'),0] for i in range(3)]
        for i in range(1,len(prices)+1):
            for j in range(1,3):
                memo[j][0]=max(memo[j][0],memo[j-1][1]-prices[i-1])
                memo[j][1]=max(memo[j][1],memo[j][0]+prices[i-1])
        return memo[-1][-1]
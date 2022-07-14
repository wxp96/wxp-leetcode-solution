from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo=[[-float('inf'),0] for i in range(len(prices)+1)]
        for i in range(1,len(prices)+1):
            memo[i][0]=max(memo[i-1][0],memo[i-2][1]-prices[i-1])
            memo[i][1]=max(memo[i-1][1],memo[i-1][0]+prices[i-1])
        return memo[-1][-1]
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=-float('inf')
        sell=0
        for i in range(len(prices)):
            buy=max(buy,-prices[i])
            sell=max(sell,prices[i]+buy)
        return sell
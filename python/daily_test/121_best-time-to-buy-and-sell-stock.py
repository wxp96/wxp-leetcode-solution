from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre_buy=-float('inf')
        pre_sell=0
        for i in range(len(prices)):
            cur_buy=max(pre_buy,-prices[i])
            cur_sell=max(pre_sell,prices[i]+pre_buy)
            pre_buy,pre_sell=cur_buy,cur_sell
        return cur_sell
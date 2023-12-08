from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre_buy=-float('inf')
        pre_sell=0
        for price in prices:
            cur_buy=max(pre_buy,pre_sell-price)
            cur_sell=max(pre_sell,pre_buy+price)
            pre_buy,pre_sell=cur_buy,cur_sell
        return cur_sell

s=Solution()
print(s.maxProfit([7,1,5,3,6,4]))
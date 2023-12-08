from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #定义memo[i][0]为卖出股票 memo[i][1]为买入股票
        memo=[[0]*2 for i in range(len(prices)+1)]
        for i in range(1,len(prices)+1):
            if i==1:
                memo[i][0]=0
                memo[i][1]=-prices[0]
                continue
            memo[i][0]=max(memo[i-1][0],prices[i-1]+memo[i-1][1])
            memo[i][1]=max(memo[i-1][1],-prices[i-1]+memo[i-2][0])
        return memo[-1][0]
    
s=Solution()
print(s.maxProfit([2,1,4]))

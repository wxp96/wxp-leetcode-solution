from typing import List
from copy import deepcopy
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp_table=[[[0,-float("inf")] for p in range(len(prices)+1)] for q in range(2)]
        for i in range(0,k+1):
            for j in range(0,len(prices)):
                dp_table[1][j+1][0]=max(dp_table[0][j][1]+prices[j],dp_table[1][j][0])
                dp_table[1][j+1][1]=max(dp_table[1][j][1],dp_table[1][j][0]-prices[j])
            dp_table[0]=deepcopy(dp_table[1])
        return dp_table[1][len(prices)][0]

s=Solution()
print(s.maxProfit(2,
[3,3,5,0,0,3,1,4]))
            
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo=[-1]*(amount+1)
        memo[0]=0
        for i in range(1,amount+1):
            if i in coins:
                memo[i]=1
                continue
            tmp=float('inf')
            for coin in coins:
                if i-coin>=0:
                    tmp=min(tmp,memo[i-coin])
            memo[i]=tmp+1
        return memo[-1] if memo[-1]!=float('inf') else -1

s=Solution()
print(s.coinChange([2],3))
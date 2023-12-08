from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        memo=[-1]*amount
        for i in range(amount):
            if i+1 in coins:
                memo[i]=1
                continue
            for j in coins:
                if i-j>=0 and memo[i-j]!=-1:
                    if memo[i]==-1:
                        memo[i]=float('inf')
                    memo[i]=min(memo[i],memo[i-j]+1)
        return memo[-1]
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins=sorted(coins,reverse=True)
        if not coins:
            return -1
            
        def dp(amount):
            if amount==0:
                return 0
            if amount < 0:
                return float('inf')
            if amount in memo.keys():
                return memo[amount]
            res=float('inf')
            for num in coins:
                res=min(dp(amount-num)+1,res)
            memo[amount]=res
            return res
        
        memo=dict()
        a=dp(amount)
        if a==float('inf'):
            return -1
        return a

s=Solution()
print(s.coinChange([2],3))
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo=[0]*(amount+1)
        memo[0]=1
        for i in range(len(coins)):
            for j in range(1,amount+1):
                if coins[i]<=j:
                    memo[j]+=memo[j-coins[i]]
        return memo[-1]
        
        # '''
        #   get the combination
        # '''
        # def dp(capacity,last_coin):
        #     if capacity<coins[last_coin]:
        #         return None
        #     if (capacity,last_coin) in memo.keys():
        #         return memo[(capacity,last_coin)]
        #     cur=[]
        #     for i in range(last_coin,len(coins)):
        #         if capacity==coins[i]:
        #             cur.append([coins[i]])
        #             break
        #         else:
        #             next=dp(capacity-coins[i],i)
        #             if not next:
        #                 continue
        #             for item in next:
        #                 cur.append([coins[i]]+item)
        #     memo[(capacity,last_coin)]=cur
        #     return cur
        
        # coins=sorted(coins)
        # memo=dict()
        # return dp(amount,0)

s=Solution()
print(s.change(10,[1,2,5]))
from typing import List
import bisect
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        ans=[]
        memo=[]
        for i,ch in enumerate(s):
            if ch == "|":
                memo.append(i)
        for l,r in queries:
            x=bisect.bisect_left(memo,l)
            y=bisect.bisect_left(memo,r)
            if s[r]=="*" and y-1>=x:
                y-=1
            if x>=len(memo):
                ans.append(0)
                break
            count=memo[y]-memo[x]-1-(y-x-1)
            ans.append(count)
        return ans

s=Solution()
print(s.platesBetweenCandles("||*",
[[2,2]]))
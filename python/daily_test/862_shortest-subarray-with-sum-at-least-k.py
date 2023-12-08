from collections import deque
from typing import List
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pre_sum=[0]
        for num in nums:
            pre_sum.append(pre_sum[-1]+num)
        q=deque()
        res=len(nums)
        for i,p in enumerate(pre_sum):
            while q and p-pre_sum[q[0]]>=k:
                res=min(res,i-q[0])
                q.popleft()
            while q and pre_sum[q[-1]]>=p:
                q.pop()
            q.append(i)
        return -1 if res==len(nums) and pre_sum[-1]<k else res

s=Solution()
print(s.shortestSubarray([84,-37,32,40,95],167))
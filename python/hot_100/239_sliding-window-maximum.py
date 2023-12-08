from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def stackapp(num,i):
            while dq and num>=dq[-1]:
                dq.pop()
                dqi.pop()
            dq.append(num)
            dqi.append(i)
            if i-dqi[0]>=k:
                dq.popleft()
                dqi.popleft()
        dq=deque()
        dqi=deque()
        res=[]
        for i in range(k):
            stackapp(nums[i],i)
        res.append(dq[0])
        for i in range(len(nums)):
            stackapp(nums[i],i)
            res.append(dq[0])
        return res

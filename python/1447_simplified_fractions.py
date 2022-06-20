from email.policy import default
from typing import List
import math
import heapq
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if n==1:
            return []
        hq=[]
        d={}
        ans=[]
        for i in range(2,n+1):
            j=1
            while j<i:
                if j/i in d.keys():
                    j+=1
                    continue
                hq.append(j/i)
                d[j/i]="{}/{}".format(j,i)
                j+=1
        heapq.heapify(hq)
        pre=heapq.heappop(hq)
        while hq:
            next=heapq.heappop(hq)
            if math.isclose(pre,next) and d[pre].split("/")[0]>d[next].split("/")[0]:
                pre=next
            else:
                ans.append(d[pre])
                pre=next
        ans.append(d[pre])
        return ans
s=Solution()
print(s.simplifiedFractions(4))
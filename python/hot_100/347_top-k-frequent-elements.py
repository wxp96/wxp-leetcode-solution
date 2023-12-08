from typing import List
from collections import defaultdict,Counter,deque
from random import randint
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def quicksort(l,k):
            if k==1 and len(l)==1:
                return l[0]
            i=randint(0,len(l)-1)
            l[i],l[-1]=l[-1],l[i]
            m=0
            for j in range(len(l)-1):
                if l[j]>l[-1]:
                    l[j],l[m]=l[m],l[j]
                    m+=1
            l[-1],l[m]=l[m],l[-1]
            if m+1==k:
                return l[m]
            elif m>=k:
                return quicksort(l[:m],k)
            else:
                return quicksort(l[m+1:],k-m-1)

        num2cnt=Counter(nums)
        cnt2num=defaultdict(deque)
        for key,v in num2cnt.items():
            cnt2num[v].append(key)
        cnts=list(num2cnt.values())
        res=[]
        ret=quicksort(cnts,k)
        for cnt in cnts:
            if cnt>=ret:
                res.append(cnt2num[cnt][-1])
                cnt2num[cnt].pop()
        return res

s=Solution()
print(s.topKFrequent([1,2],2))     
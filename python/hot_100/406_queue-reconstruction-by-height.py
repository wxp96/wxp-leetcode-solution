from typing import List
# from collections import deque
# import bisect
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0],x[1]))
        height=[]
        for h,k in people:
            if not height:
                height.append((h,k))
                continue
            cnt=0
            ins=False
            for i,(hi,ki) in enumerate(height):
                if cnt==k:
                    height.insert(i,(h,k))
                    ins=True
                    break
                if hi >=h:
                    cnt+=1
            if not ins:
                height.append((h,k))
        return height
    
s=Solution()
print(s.reconstructQueue([[1,0],[2,0]]))


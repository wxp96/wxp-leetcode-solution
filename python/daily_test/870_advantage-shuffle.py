from typing import List
from collections import defaultdict
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3=sorted(nums2)
        d=defaultdict(list)
        nums1.sort()
        i=j=0
        tmp=[]
        while i<len(nums3) and j<len(nums1):
            while j<len(nums1):
                if nums1[j]<=nums3[i]:
                    tmp.append(nums1[j])
                    j+=1
                else:
                    d[nums3[i]].append(nums1[j])
                    j+=1
                    i+=1
                    break
        nums3=[]
        for num in nums2:
            if num not in d.keys():
                nums3.append(tmp.pop())
            else:
                nums3.append(d[num].pop())
        return nums3

s=Solution()
print(s.advantageCount([2,0,4,1,2],[1,3,0,0,2]))
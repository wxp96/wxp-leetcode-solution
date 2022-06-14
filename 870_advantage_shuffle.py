from typing import List
from collections import deque,defaultdict
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3=nums2[:]
        nums3.sort()
        nums1.sort()
        d1=defaultdict(deque)
        d2=deque()
        i=0
        for num in nums1:
            if nums3[i]<num:
                d1[nums3[i]].append(num)
                i+=1
            else:
                d2.append(num)
        for i in range(len(nums1)):
            if len(d1[nums2[i]])!=0:
                nums1[i]=d1[nums2[i]].pop()
            else:
                nums1[i]=d2.pop()
        return nums1

s=Solution()
print(s.advantageCount([2,0,4,1,2],[1,3,0,0,2]))
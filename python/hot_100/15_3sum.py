from typing import List
from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        dd=defaultdict(list)
        for i,num in enumerate(nums):
            dd[num].append(i)
        res=[]
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j!=i+1 and nums[j]==nums[j-1]:
                    continue
                two=-(nums[i]+nums[j])
                if two in dd.keys():
                    for k in dd[two]:
                        if k>i and k>j:
                            res.append([nums[i],nums[j],nums[k]])
                            break
        return res

s=Solution()
print(s.threeSum([0,0,0,0]))
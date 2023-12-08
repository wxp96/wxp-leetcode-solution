from functools import reduce
class Solution:
    def maximumSwap(self, num: int) -> int:
        nums=[int(n) for n in str(num)]
        nums1=nums[:]
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if nums[i]!=nums1[i]:
                for j in range(len(nums1)-1,0,-1):
                    if nums1[j]==nums[i]:
                        nums1[i],nums1[j]=nums1[j],nums1[i]
                        break
                break
        return reduce(lambda x,y:x*10+y,nums1)
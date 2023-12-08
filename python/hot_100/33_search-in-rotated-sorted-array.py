from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)
        if nums[0]>target>nums[-1]:
            return -1
        while l<r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                if nums[mid]>=nums[0] or target<=nums[-1]:
                    l=mid+1
                elif target>=nums[0]>nums[mid]:
                    r=mid
            elif nums[mid]>target:
                if target>=nums[0] or nums[-1]>=nums[mid]:
                    r=mid
                elif nums[mid]>=nums[0]>target:
                    l=mid+1
        return -1

s=Solution()
print(s.search([1],1))


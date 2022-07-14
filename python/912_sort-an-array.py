from typing import List
import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # '''
        # quick sort
        # '''
        # if not nums:
        #     return nums
        # seed=random.randint(0,len(nums)-1)
        # nums[seed],nums[-1]=nums[-1],nums[seed]
        # j=0
        # for i in range(len(nums)-1):
        #     if nums[i]<nums[-1]:
        #         nums[i],nums[j]=nums[j],nums[i]
        #         j+=1
        # nums[j],nums[-1]=nums[-1],nums[j]
        # return self.sortArray(nums[:j])+[nums[j]]+self.sortArray(nums[j+1:len(nums)])

        '''
        mergesort
        '''

        def merge(left,right):
            l=0
            l_end=len(left)
            r=0
            r_end=len(right)
            tmp=[]
            while l<l_end and r<r_end:
                if left[l]<right[r]:
                    tmp.append(left[l])
                    l+=1
                else:
                    tmp.append(right[r])
                    r+=1
            if l<=mid:
                tmp+=left[l:]
            else:
                tmp+=right[r:]
            return tmp

        if len(nums)==1:
            return nums
        l,r=0,len(nums)-1
        mid=r//2
        left=self.sortArray(nums[l:mid+1])
        right=self.sortArray(nums[mid+1:r+1])
        return merge(left,right)

s=Solution()
s.sortArray([5,1,1,2,0,0])
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length=len(nums)
        res=[]
        def backtrack(i):
            if i == length-1:
                res.append(nums[:])
                return
            for j in range(i,length):
                if j != i and nums[j]==nums[j-1]:
                    continue
                tmp=nums[j]
                for k in range(j,i,-1):
                    nums[k]=nums[k-1]
                nums[i]=tmp
                backtrack(i+1)
                for k in range(i,j):
                    nums[k]=nums[k+1]
                nums[j]=tmp

        backtrack(0)
        return res

s=Solution()
print(s.permuteUnique([0,1,0,0,9]))
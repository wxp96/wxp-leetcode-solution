from typing import List
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        nums_r=nums[::-1]
        max_num=[]
        for i in range(len(nums_r)):
            if i == 0 or nums_r[i]>max_num[-1]:
                max_num.append(nums_r[i])
            else:
                max_num.append(max_num[-1])
        max_num=max_num[::-1]
        rs=-1
        for i in range(len(nums)):
            if max_num[i]>nums[i]:
                rs=max(rs,max_num[i]-nums[i])
        return rs
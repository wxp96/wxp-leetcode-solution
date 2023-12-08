from typing import List
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        max_left=cur_left=num[0]
        pos=0
        for i,num in enumerate(nums):
            if num<cur_left:
                pos=i+1
                cur_left=max_left
            max_left=max(max_left,num)
            
        return pos
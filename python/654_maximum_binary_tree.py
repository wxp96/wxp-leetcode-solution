import sys
sys.path.append(r"D:\code\leetcode")
from python.lc_utils import TreeNode
from typing import List
from collections import deque
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # index={num:i for i,num in enumerate(nums)}
        # def inner(nums):
        #     if not nums:
        #         return None
        #     root=TreeNode(max(nums))
        #     i=index[max(nums)]-index[nums[0]]
        #     root.left=inner(nums[:i])
        #     root.right=inner(nums[i+1:len(nums)])
        #     return root

        # return inner(nums)
        stack=deque()
        for num in nums:
            littler=None
            num = TreeNode(num)
            while stack and stack[-1].val<num.val:
                littler=stack.pop()
            if stack:
                stack[-1].right=num
            num.left=littler
            stack.append(num)
        return stack[0]
            
s=Solution()
s.constructMaximumBinaryTree(nums = [3,2,1,6,0,5])
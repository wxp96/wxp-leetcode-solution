from typing import List
# class NumArray:
#     '''
#         segment tree
#     '''
#     def __init__(self, nums: List[int]):
#         self.ori_len=len(nums)
#         self.tree=[0]*len(nums)+nums
#         for i in range(len(nums)-1,0,-1):
#             self.tree[i]=self.tree[2*i]+self.tree[2*i+1]

#     def update(self, index: int, val: int) -> None:
#         i=self.ori_len+index
#         self.tree[i]=val
#         i=i>>1
#         while i>0:
#             self.tree[i]=self.tree[2*i]+self.tree[2*i+1]
#             i=i>>1

#     def sumRange(self, left: int, right: int) -> int:
#         res=0
#         left+=self.ori_len
#         right+=self.ori_len
#         while left<=right:
#             if left&1:
#                 res+=self.tree[left]
#                 left+=1
#             if not right&1:
#                 res+=self.tree[right]
#                 right-=1
#             left=left>>1
#             right=right>>1
#         return res

class NumArray:
    '''
    binary indexed tree
    '''
    def __init__(self, nums: List[int]):
        self.nums=nums
        self.tree=[0]*(len(nums)+1)
        for i,num in enumerate(nums):
            self.set(i,num)

    def lowbit(self,x):
        return x&(-x)

    def set(self,index,delta):
        index=index+1
        while index<len(self.tree):
            self.tree[index]+=delta
            index+=self.lowbit(index)

    def update(self, index: int, val: int) -> None:
        delta=val-self.nums[index]
        self.nums[index]=val
        self.set(index,delta)

    def sumRange(self, left: int, right: int) -> int:
        l,r=left,right+1
        left_sum=0
        while l>0:
            left_sum+=self.tree[l]
            l-=self.lowbit(l)
        right_sum=0
        while r>0:
            right_sum+=self.tree[r]
            r-=self.lowbit(r)
        return right_sum-left_sum

# ["NumArray","update","update","update","sumRange","update","sumRange","update","sumRange","sumRange","update"]
# [[[7,2,7,2,0]],[4,6],[0,2],[0,9],[4,4],[3,8],[0,4],[4,1],[0,3],[0,4],[0,4]]

numarray=NumArray([7,2,7,2,0])

numarray.update(4,6)#7 2 7 2 6
print(numarray.sumRange(4,4))
numarray.update(3,8)#9 2 7 8 6
numarray.sumRange(0,4)
numarray.update(4,1)
numarray.sumRange(0,3)
numarray.sumRange(0,4)
numarray.update(0,4)
numarray=NumArray([1,3,5,7,9,11])
numarray.sumRange(2,5)
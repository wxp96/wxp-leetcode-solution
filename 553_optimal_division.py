from typing import List
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        def max_division(x,y):
            if x==y:
                return nums[x],str(nums[x])
            if (x,y) in dp_max.keys():
                return dp_max[(x,y)]
            rs_max=0
            rs_str=""
            for i in range(x,y):
                left=max_division(x,i)
                right=min_division(i+1,y)
                if left[0]/right[0]>rs_max:
                    rs_max=left[0]/right[0]
                    if i!=y-1:
                        rs_str=left[1]+"/"+"("+right[1]+")"
                    else:
                        rs_str=left[1]+"/"+right[1]
            dp_max[(x,y)]=rs_max,rs_str
            return rs_max,rs_str

        def min_division(x,y):
            if x==y:
                return nums[x],str(nums[x])
            if (x,y) in dp_min.keys():
                return dp_min[(x,y)]
            rs_min=float("inf")
            rs_str=""
            for i in range(x,y):
                left=min_division(x,i)
                right=max_division(i+1,y)
                if left[0]/right[0]<rs_min:
                    rs_min=left[0]/right[0]
                    if i!=y-1:
                        rs_str=left[1]+"/"+"("+right[1]+")"
                    else:
                        rs_str=left[1]+"/"+right[1]
            dp_min[(x,y)]=rs_min,rs_str
            return rs_min,rs_str
        
        dp_max={}
        dp_min={}
        return max_division(0,len(nums)-1)[1]

s=Solution()
print(s.optimalDivision([1000,100,10,2]))
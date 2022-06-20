class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        def dp(k,i,j):
            rs=0
            if k==0:
                return 1
            if (k,i,j) in dp_table.keys():
                return dp_table[(k,i,j)]
            else:
                for x,y in[(1,2),(2,1),(-1,2),(1,-2),(-2,1),(2,-1),(-1,-2),(-2,-1)]:
                    if 0<=i+x<n and 0<=j+y<n:
                        dp_table[(k,i+x,j+y)]=dp(k-1,i+x,j+y)/8
                        rs+=dp_table[(k,i+x,j+y)]
            return rs

        dp_table=dict()
        return dp(k,row,column)


s=Solution()
print(s.knightProbability(4,3,2,2))
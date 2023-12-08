class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [1,2]:
            return n
        memo=[0]*n
        memo[0],memo[1]=1,2
        for i in range(2,n):
            memo[i]=memo[i-1]+memo[i-2]
        return memo[-1]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo=[1]*n
        for i in range(1,m):
            for j in range(1,n):
                memo[j]=memo[j]+memo[j-1]
        return memo[-1]